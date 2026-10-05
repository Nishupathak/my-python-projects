import csv
import datetime
import os

FILE = "expenses.csv"


def load_expenses():
    expenses = []
    if not os.path.exists(FILE):
        return expenses
    with open(FILE, "r", newline="") as f:
        for row in csv.reader(f):
            if len(row) == 4:
                date, category, amount, note = row
                expenses.append(
                    {"date": date, "category": category,
                     "amount": float(amount), "note": note}
                )
    return expenses


def save_expenses(expenses):
    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        for e in expenses:
            writer.writerow([e["date"], e["category"], e["amount"], e["note"]])


def add_expense(expenses):
    category = input("Category (food, travel, fun...): ").strip().title()
    if category == "":
        print("Category can't be empty.")
        return
    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("Please type a number!")
        return
    if amount <= 0:
        print("Amount must be more than 0.")
        return
    note = input("Note (optional): ").strip()
    today = str(datetime.date.today())
    expenses.append(
        {"date": today, "category": category, "amount": amount, "note": note}
    )
    save_expenses(expenses)
    print("Saved!")


def show_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses yet!")
        return
    for number, e in enumerate(expenses, start=1):
        print(number, "|", e["date"], "|", e["category"], "|",
              e["amount"], "|", e["note"])
    total = sum(e["amount"] for e in expenses)
    print("Total spent:", round(total, 2))


def show_summary(expenses):
    if len(expenses) == 0:
        print("No expenses yet!")
        return
    totals = {}
    for e in expenses:
        cat = e["category"]
        totals[cat] = totals.get(cat, 0) + e["amount"]
    grand = sum(totals.values())
    for cat, money in sorted(totals.items(), key=lambda item: item[1], reverse=True):
        percent = money * 100 / grand
        print(cat, ":", round(money, 2), "(" + str(round(percent)) + "%)")
    print("Total:", round(grand, 2))


def delete_expense(expenses):
    show_expenses(expenses)
    if len(expenses) == 0:
        return
    try:
        number = int(input("Which number to delete? "))
    except ValueError:
        print("Please type a number!")
        return
    if 1 <= number <= len(expenses):
        expenses.pop(number - 1)
        save_expenses(expenses)
        print("Deleted!")
    else:
        print("That number isn't on the list.")


expenses = load_expenses()

while True:
    print()
    print("1 = add, 2 = show all, 3 = summary, 4 = delete, 5 = quit")
    choice = input("Pick: ")
    if choice == "1":
        add_expense(expenses)
    elif choice == "2":
        show_expenses(expenses)
    elif choice == "3":
        show_summary(expenses)
    elif choice == "4":
        delete_expense(expenses)
    elif choice == "5":
        print("Bye!")
        break
    else:
        print("Please pick 1 to 5.")