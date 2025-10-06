from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types import AudioPiped
from yt_dlp import YoutubeDL
import os

from config import Config

# --- Setup ---
API_ID = Config.API_ID
API_HASH = Config.API_HASH
SESSION_STRING = ""  # add your user session string (for VC join)
USERBOT = Client("UserBot", api_id=API_ID, api_hash=API_HASH, session_string=SESSION_STRING)
pytgcalls = PyTgCalls(USERBOT)

# --- Download dir ---
if not os.path.exists("downloads"):
    os.makedirs("downloads")

ydl_opts = {
    "format": "bestaudio/best",
    "outtmpl": "downloads/%(title)s.%(ext)s",
    "quiet": True,
    "nocheckcertificate": True,
}

def download_audio(query):
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(query, download=True)
        return ydl.prepare_filename(info)

@Client.on_message(filters.command("play") & filters.group)
async def play_music(client, message):
    if len(message.command) < 2:
        return await message.reply("Usage: `/play <song name or YouTube URL>`")

    query = " ".join(message.command[1:])
    msg = await message.reply(f"🔍 Searching `{query}` ...")

    try:
        file = download_audio(query)
        await msg.edit("🎶 Download complete, joining VC...")

        chat_id = message.chat.id
        await pytgcalls.join_group_call(chat_id, AudioPiped(file))
        await msg.edit(f"🎧 Now playing: **{os.path.basename(file)}**")
    except Exception as e:
        await msg.edit(f"❌ Error: `{e}`")

@Client.on_message(filters.command("stop") & filters.group)
async def stop_music(client, message):
    chat_id = message.chat.id
    await pytgcalls.leave_group_call(chat_id)
    await message.reply("⏹️ Stopped playback and left VC.")
