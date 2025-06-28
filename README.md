# NoteApp

A simple command-line application to track income, expenses and invoice reminders.

## Features
- Record income and attach an invoice image path
- Record expenses and attach an invoice image path
- Create reminders for invoices
- List and complete reminders

## Usage

Initialize the database:

```bash
python -m noteapp.cli init
```

Add an income record:

```bash
python -m noteapp.cli add-income 1500 --description "Website project" --image path/to/invoice.png
```

Add an expense record:

```bash
python -m noteapp.cli add-expense 200 --description "Office supplies" --image path/to/receipt.jpg
```

Add a reminder:

```bash
python -m noteapp.cli add-reminder "Send monthly invoice" --due 2024-05-01
```

List incomes, expenses and reminders:

```bash
python -m noteapp.cli list-income
python -m noteapp.cli list-expense
python -m noteapp.cli list-reminders --all
```

Mark a reminder completed:

```bash
python -m noteapp.cli complete-reminder 1
```
