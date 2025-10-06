from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types import AudioPiped
from yt_dlp import YoutubeDL
from MukeshRobot.config import Config
import os

# Initialize userbot for VC
userbot = Client("MukeshUserbot", api_id=Config.API_ID, api_hash=Config.API_HASH, session_string=Config.SESSION_STRING)
pytgcalls = PyTgCalls(userbot)

# Create downloads folder
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
    msg = await message.reply(f"🎵 Searching `{query}`...")

    try:
        file = download_audio(query)
        await msg.edit("📥 Download complete! Joining VC...")

        chat_id = message.chat.id
        await pytgcalls.join_group_call(chat_id, AudioPiped(file))
        await msg.edit(f"🎶 Now playing: **{os.path.basename(file)}**")
    except Exception as e:
        await msg.edit(f"❌ Error: `{e}`")

@Client.on_message(filters.command("pause") & filters.group)
async def pause_music(client, message):
    try:
        await pytgcalls.pause_stream(message.chat.id)
        await message.reply("⏸️ Music paused.")
    except:
        await message.reply("❌ Not playing anything.")

@Client.on_message(filters.command("resume") & filters.group)
async def resume_music(client, message):
    try:
        await pytgcalls.resume_stream(message.chat.id)
        await message.reply("▶️ Music resumed.")
    except:
        await message.reply("❌ Nothing to resume.")

@Client.on_message(filters.command("stop") & filters.group)
async def stop_music(client, message):
    try:
        await pytgcalls.leave_group_call(message.chat.id)
        await message.reply("⏹️ Stopped playback and left VC.")
    except:
        await message.reply("❌ Already not in VC.")
