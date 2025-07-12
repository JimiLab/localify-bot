import asyncio
from commands import bot
from config import BOT_TOKEN
from api import serve_api


async def main():
    await asyncio.gather(
        bot.start(BOT_TOKEN),
        serve_api(),
    )

if __name__ == "__main__":
    asyncio.run(main())
