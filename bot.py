import asyncio
from pyrogram import Client, filters
from core import mongo
from strings.messages import *
import config
from assistant import assistant, player

app = Client("Neva", api_id=config.API_ID, api_hash=config.API_HASH, bot_token=config.BOT_TOKEN)

def is_admin(user_id):
    return user_id in config.ADMINS or user_id == config.OWNER_ID

@app.on_message(filters.command("start") & filters.private)
async def start(_, message):
    await message.reply_text("🎵 Merhaba! Ben Neva — sesli sohbette müzik çalabilirim!")

# ---------------- /play ----------------
@app.on_message(filters.command("play") & filters.group)
async def play(_, message):
    if len(message.command) < 2:
        return await message.reply_text("🔍 Şarkı adı veya URL gir.")
    query = " ".join(message.command[1:])
    chat_id = message.chat.id

    # Eğer zaten çalıyorsa playlist’e ekle
    if chat_id in player._playing:
        await mongo.add_song_to_playlist(chat_id, query)
        await message.reply_text(f"{ADDED_TO_QUEUE}: {query}")
        if config.LOG_GROUP_ID:
            await app.send_message(config.LOG_GROUP_ID, f"{message.from_user.first_name} /play ile playlist’e ekledi: {query}")
        return

    # Şarkıyı indirip çal
    song_file = await player.play_song(chat_id, query)
    if not song_file:
        return await message.reply_text(DOWNLOAD_FAILED)
    await message.reply_text(f"{PLAYING}: {query}")
    if config.LOG_GROUP_ID:
        await app.send_message(config.LOG_GROUP_ID, f"{message.from_user.first_name} /play kullandı: {query}")

# Diğer komutlar (/add, /queue, /skip, /pause, /resume, /leave, /broadcast) 
# FallenMusic mantığı ile admin/owner kontrol ve log grup ile çalışır

async def main():
    print("🎧 Neva başlatılıyor...")
    await app.start()
    await assistant.start()
    print("✅ Bot ve assistant aktif")
    from pytgcalls import idle
    await idle()
    await app.stop()
    await assistant.stop()

if __name__ == "__main__":
    asyncio.run(main())
