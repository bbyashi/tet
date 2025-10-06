from pyrogram import Client, filters
from pytgcalls import PyTgCalls, idle
from pytgcalls.types import InputAudioStream, AudioPiped
from yt_dlp import YoutubeDL
import os

# --- CONFIG ---
API_ID = 123456       # apna API ID (from my.telegram.org)
API_HASH = "your_api_hash"
SESSION_STRING = "your_pyrogram_string_session"  # generate via Pyrogram
bot = Client("VCPlayerBot", api_id=API_ID, api_hash=API_HASH, session_string=SESSION_STRING)

# --- PyTgCalls Init ---
pytgcalls = PyTgCalls(bot)

# --- YT-DLP Options ---
ydl_opts = {
    "format": "bestaudio/best",
    "outtmpl": "downloads/%(title)s.%(ext)s",
    "quiet": True,
    "nocheckcertificate": True,
}

if not os.path.exists("downloads"):
    os.makedirs("downloads")

# --- Function to Download Audio ---
def download_audio(query):
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(query, download=True)
        file_name = ydl.prepare_filename(info)
    return file_name

# --- PLAY Handler ---
@bot.on_message(filters.command("play") & filters.group)
async def play_handler(client, message):
    if len(message.command) < 2:
        return await message.reply("❌ Usage: `/play <song name or YouTube URL>`")

    query = " ".join(message.command[1:])
    msg = await message.reply(f"🎵 Searching `{query}` ...")

    try:
        # Download audio
        file = download_audio(query)
        await msg.edit("📥 Downloaded successfully! Joining VC...")

        chat_id = message.chat.id
        await pytgcalls.join_group_call(
            chat_id,
            AudioPiped(file),
        )
        await msg.edit(f"🎧 Now playing: **{os.path.basename(file)}**")
    except Exception as e:
        await msg.edit(f"❌ Error: `{e}`")

# --- END / STOP Handler ---
@bot.on_message(filters.command("stop") & filters.group)
async def stop_handler(client, message):
    chat_id = message.chat.id
    await pytgcalls.leave_group_call(chat_id)
    await message.reply("⏹️ Stopped playback and left VC.")

# --- Start bot ---
async def main():
    await bot.start()
    await pytgcalls.start()
    print("🎶 VC Player running...")
    await idle()
    await bot.stop()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
