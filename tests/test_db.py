import os
from pathlib import Path
from noteapp import db

TEST_DB = Path(__file__).parent / "test.db"


def setup_module(module):
    if TEST_DB.exists():
        TEST_DB.unlink()
    db.init_db(TEST_DB)


def teardown_module(module):
    if TEST_DB.exists():
        TEST_DB.unlink()


def test_add_and_list_income():
    db.add_income(100.0, "Test income", db_path=TEST_DB)
    rows = db.list_income(db_path=TEST_DB)
    assert len(rows) == 1
    assert rows[0]["amount"] == 100.0


def test_add_and_list_expense():
    db.add_expense(50.0, "Test expense", db_path=TEST_DB)
    rows = db.list_expense(db_path=TEST_DB)
    assert len(rows) == 1
    assert rows[0]["amount"] == 50.0


def test_add_and_complete_reminder():
    db.add_reminder("Pay bill", "2024-01-01", db_path=TEST_DB)
    rows = db.list_reminders(db_path=TEST_DB, include_completed=False)
    assert len(rows) == 1
    rid = rows[0]["id"]
    db.complete_reminder(rid, db_path=TEST_DB)
    rows2 = db.list_reminders(db_path=TEST_DB, include_completed=False)
    assert len(rows2) == 0
