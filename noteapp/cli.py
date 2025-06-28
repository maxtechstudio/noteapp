import argparse
from pathlib import Path
from . import db


def init(args):
    db.init_db()
    print("Database initialized at", db.DB_PATH)


def add_income_cmd(args):
    db.add_income(args.amount, args.description, args.image)
    print("Income added.")


def list_income_cmd(args):
    rows = db.list_income()
    for row in rows:
        print(f"[{row['id']}] ${row['amount']:.2f} - {row['description']} image: {row['image_path']} at {row['created_at']}")


def add_expense_cmd(args):
    db.add_expense(args.amount, args.description, args.image)
    print("Expense added.")


def list_expense_cmd(args):
    rows = db.list_expense()
    for row in rows:
        print(f"[{row['id']}] ${row['amount']:.2f} - {row['description']} image: {row['image_path']} at {row['created_at']}")


def add_reminder_cmd(args):
    db.add_reminder(args.description, args.due)
    print("Reminder added.")


def list_reminder_cmd(args):
    rows = db.list_reminders(include_completed=args.all)
    for row in rows:
        status = "done" if row['completed'] else "pending"
        print(f"[{row['id']}] {row['description']} due: {row['due_date']} status: {status}")


def complete_reminder_cmd(args):
    db.complete_reminder(args.id)
    print("Reminder completed.")


def build_parser():
    parser = argparse.ArgumentParser(description="Note app for income, expenses, and reminders")
    sub = parser.add_subparsers()

    init_p = sub.add_parser('init', help='initialize database')
    init_p.set_defaults(func=init)

    inc_add = sub.add_parser('add-income', help='add income record')
    inc_add.add_argument('amount', type=float, help='income amount')
    inc_add.add_argument('--description', default='', help='description')
    inc_add.add_argument('--image', help='path to invoice image')
    inc_add.set_defaults(func=add_income_cmd)

    inc_list = sub.add_parser('list-income', help='list income records')
    inc_list.set_defaults(func=list_income_cmd)

    exp_add = sub.add_parser('add-expense', help='add expense record')
    exp_add.add_argument('amount', type=float, help='expense amount')
    exp_add.add_argument('--description', default='', help='description')
    exp_add.add_argument('--image', help='path to invoice image')
    exp_add.set_defaults(func=add_expense_cmd)

    exp_list = sub.add_parser('list-expense', help='list expense records')
    exp_list.set_defaults(func=list_expense_cmd)

    rem_add = sub.add_parser('add-reminder', help='add invoice reminder')
    rem_add.add_argument('description', help='reminder description')
    rem_add.add_argument('--due', help='due date')
    rem_add.set_defaults(func=add_reminder_cmd)

    rem_list = sub.add_parser('list-reminders', help='list reminders')
    rem_list.add_argument('--all', action='store_true', help='include completed reminders')
    rem_list.set_defaults(func=list_reminder_cmd)

    rem_done = sub.add_parser('complete-reminder', help='mark reminder as completed')
    rem_done.add_argument('id', type=int, help='reminder id')
    rem_done.set_defaults(func=complete_reminder_cmd)

    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
