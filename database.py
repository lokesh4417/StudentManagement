
import sqlite3
from contextlib import contextmanager

DATABASE = "students.db"


@contextmanager
def get_db():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row

    try:
        yield connection
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()


def init_db():
    with get_db() as connection:
        # Create the table if it does not exist.
        connection.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                department TEXT NOT NULL
            )
        """)

        # Add missing columns to an existing database.
        columns = {
            row["name"]
            for row in connection.execute(
                "PRAGMA table_info(students)"
            ).fetchall()
        }

        if "email" not in columns:
            connection.execute(
                "ALTER TABLE students ADD COLUMN email TEXT"
            )

        if "password" not in columns:
            connection.execute(
                "ALTER TABLE students ADD COLUMN password TEXT"
            )


if __name__ == "__main__":
    init_db()
    print("Database initialized successfully.")
