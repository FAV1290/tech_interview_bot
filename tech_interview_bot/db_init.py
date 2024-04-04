from sqlite3 import Cursor, connect
from typing import Iterator
from contextlib import contextmanager

from .constants import SQLITE_DB_FILEPATH


@contextmanager
def init_sqlite_connection_cursor(
    db_filepath: str = SQLITE_DB_FILEPATH,
) -> Iterator[Cursor]:
    try:
        connection = connect(db_filepath)
        cursor = connection.cursor()
        yield cursor
    finally:
        connection.close()
