import asyncio
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from chatgpt import web_server

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="chatgpt",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=200,
            plugins={"root": "chatgpt"},
            sleep_threshold=15,
        )

    async def start(self, **kwargs):
        # Make sure we don't create a new event loop here
        await super().start()
        me = await self.get_me()
        print(f"{me.first_name} Now Working 😘")

if __name__ == "__main__":
    # Use asyncio.run() to properly manage the event loop
    bot = Bot()
    asyncio.run(bot.start())
