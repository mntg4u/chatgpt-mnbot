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
        # Call super().start() to initialize the bot
        await super().start()
        me = await self.get_me()     
        print(f"{me.first_name} Now Working 😘")

# Run the bot (This is handled internally by pyrogram's `run()` method)
if __name__ == "__main__":
    bot = Bot()
    bot.run()
