from aiogram.utils.markdown import hbold

from .db_models import Question


def format_tg_code_html(code_str: str) -> str:
    code_str = code_str.replace('>', '&gt;').replace('<', '&lt;')
    return f'<pre><code class="language-python">{code_str}</code></pre>'


def format_tg_spoiler_html(text_str: str) -> str:
    return f'<tg-spoiler>{text_str}</tg-spoiler>'


def compose_question_messages_queue(question_obj: Question) -> list[str]:
    messages = [hbold(f'Вопрос №{question_obj.question_id}: {question_obj.title}')]
    if question_obj.question_codebase:
        messages.append(format_tg_code_html(question_obj.question_codebase))
    if question_obj.answer:
        messages.append(format_tg_spoiler_html(question_obj.answer))
    if question_obj.codebase:
        messages.append(format_tg_code_html(question_obj.codebase))
    return messages


def is_question_id_valid(question_id: int) -> bool:
    return 1 <= question_id
