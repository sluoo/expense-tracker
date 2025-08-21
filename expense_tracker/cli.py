import argparse, sqlite3

def init_db():
    conn = sqlite3.connect("expenses.db")
    conn.execute("""CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        category TEXT,
        description TEXT,
        amount REAL
    )""")
    conn.close()

def add_expense(date, category, desc, amount):
    conn = sqlite3.connect("expenses.db")
    conn.execute(
        "INSERT INTO expenses (date, category, description, amount) VALUES (?, ?, ?, ?)",
        (date, category, desc, amount)
    )
    conn.commit()
    conn.close()
    print("Expense added!")

def list_expenses():
    conn = sqlite3.connect("expenses.db")
    rows = conn.execute("SELECT id, date, category, description, amount FROM expenses").fetchall()
    conn.close()
    for row in rows:
        print(row)

def main():
    parser = argparse.ArgumentParser(description="Simple Expense Tracker")
    sub = parser.add_subparsers(dest="command")

    p_add = sub.add_parser("add")
    p_add.add_argument("--date", required=True)
    p_add.add_argument("--category", required=True)
    p_add.add_argument("--desc", default="")
    p_add.add_argument("--amount", type=float, required=True)

    sub.add_parser("list")

    args = parser.parse_args()
    init_db()

    if args.command == "add":
        add_expense(args.date, args.category, args.desc, args.amount)
    elif args.command == "list":
        list_expenses()
