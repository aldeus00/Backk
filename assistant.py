from pyrogram import Client
from player.musicplayer import MusicPlayer
import config
import asyncio

assistant = Client(
    "assistant",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    session_string=config.ASSISTANT_SESSION
)

player = MusicPlayer(assistant)

async def start_assistant():
    await assistant.start()
    await player.start()
    print("✅ Assistant aktif ve müzik modülü hazır")
    from pytgcalls import idle
    await idle()
    await assistant.stop()

if __name__ == "__main__":
    asyncio.run(start_assistant())
