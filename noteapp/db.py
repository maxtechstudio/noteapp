import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "noteapp.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS income (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL NOT NULL,
    description TEXT,
    image_path TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS expense (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL NOT NULL,
    description TEXT,
    image_path TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS reminder (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL,
    due_date TEXT,
    completed INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

def get_connection(db_path: Path = DB_PATH):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def init_db(db_path: Path = DB_PATH):
    conn = get_connection(db_path)
    with conn:
        conn.executescript(SCHEMA)
    conn.close()

# Income operations

def add_income(amount: float, description: str = "", image_path: str = None, db_path: Path = DB_PATH):
    conn = get_connection(db_path)
    with conn:
        conn.execute(
            "INSERT INTO income (amount, description, image_path) VALUES (?, ?, ?)",
            (amount, description, image_path),
        )
    conn.close()


def list_income(db_path: Path = DB_PATH):
    conn = get_connection(db_path)
    cur = conn.execute("SELECT * FROM income ORDER BY created_at DESC")
    rows = cur.fetchall()
    conn.close()
    return rows

# Expense operations

def add_expense(amount: float, description: str = "", image_path: str = None, db_path: Path = DB_PATH):
    conn = get_connection(db_path)
    with conn:
        conn.execute(
            "INSERT INTO expense (amount, description, image_path) VALUES (?, ?, ?)",
            (amount, description, image_path),
        )
    conn.close()


def list_expense(db_path: Path = DB_PATH):
    conn = get_connection(db_path)
    cur = conn.execute("SELECT * FROM expense ORDER BY created_at DESC")
    rows = cur.fetchall()
    conn.close()
    return rows

# Reminder operations

def add_reminder(description: str, due_date: str = None, db_path: Path = DB_PATH):
    conn = get_connection(db_path)
    with conn:
        conn.execute(
            "INSERT INTO reminder (description, due_date) VALUES (?, ?)",
            (description, due_date),
        )
    conn.close()


def list_reminders(db_path: Path = DB_PATH, include_completed: bool = True):
    conn = get_connection(db_path)
    if include_completed:
        cur = conn.execute("SELECT * FROM reminder ORDER BY due_date IS NULL, due_date")
    else:
        cur = conn.execute("SELECT * FROM reminder WHERE completed = 0 ORDER BY due_date IS NULL, due_date")
    rows = cur.fetchall()
    conn.close()
    return rows


def complete_reminder(reminder_id: int, db_path: Path = DB_PATH):
    conn = get_connection(db_path)
    with conn:
        conn.execute(
            "UPDATE reminder SET completed = 1 WHERE id = ?",
            (reminder_id,),
        )
    conn.close()
