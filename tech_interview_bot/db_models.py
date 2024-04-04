import typing
import dataclasses

from .db_init import init_sqlite_connection_cursor


@dataclasses.dataclass(frozen=True, slots=True)
class Question:
    _db_table = 'question'
    question_id: int
    title: str
    question_codebase: str | None
    answer: str | None
    source: str | None
    codebase: str | None

    @staticmethod
    def _fetch_query_response(query: str) -> list[typing.Any]:
        with init_sqlite_connection_cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

    @classmethod
    def fetch_random(cls) -> typing.Self:
        query = f'''
            SELECT question_id, title, question_codebase, answer, source, codebase
            FROM {cls._db_table} ORDER BY RANDOM() LIMIT 1
        '''
        question_args = cls._fetch_query_response(query)[0]
        return cls(*question_args)

    @classmethod
    def fetch_by_id(cls, target_id: int) -> typing.Self:
        query = f'''
            SELECT question_id, title, question_codebase, answer, source, codebase
            FROM {cls._db_table} WHERE question_id = {target_id} LIMIT 1
        '''
        question_args = cls._fetch_query_response(query)[0]
        return cls(*question_args)
