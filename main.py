import asyncio
import logging
import sys

from aiogram import Bot
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from tech_interview_bot.bot_init import dp
from tech_interview_bot.constants import BOT_TOKEN


async def main() -> None:
    default_properties = DefaultBotProperties(parse_mode=ParseMode.HTML)
    bot = Bot(BOT_TOKEN, default=default_properties)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
