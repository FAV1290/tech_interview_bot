from aiogram.types import Message, LinkPreviewOptions
from aiogram import Dispatcher, types
from aiogram.filters import CommandStart, Command

from .db_models import Question
from .utils import compose_question_messages_queue

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer('Hello there!')


@dp.message(Command('random_question'))  # /random_question
async def fetch_random_handler(message: types.Message) -> None:
    random_question = Question.fetch_random()
    question_messages = compose_question_messages_queue(random_question)
    for item in question_messages:
        await message.answer(item)


@dp.message(Command('q'))  # /q 123
async def fetch_by_id_handler(message: types.Message) -> None:
    num = int(message.text.split()[1]) if message.text else 1
    target_question = Question.fetch_by_id(num)
    question_messages = compose_question_messages_queue(target_question)
    for item in question_messages:
        await message.answer(item)
