import json
import os

FILE_NAME = "expenses.json"

# Load expenses from file
def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save expenses to file
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

# Add expense
def add_expense(expenses):
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Travel, Bills, etc.): ")
    description = input("Enter description: ")
    
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Try again.")
        return

    expense = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }

    expenses.append(expense)
    save_expenses(expenses)
    print("✅ Expense added successfully!")

# View all expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print("\n===== All Expenses =====")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['date']} | {exp['category']} | {exp['description']} | ${exp['amount']}")

# Total expense
def total_expense(expenses):
    total = sum(exp["amount"] for exp in expenses)
    print(f"\n💰 Total Expense: ${total}")

# Main menu
def main():
    expenses = load_expenses()

    while True:
        print("\n==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            total_expense(expenses)
        elif choice == "4":
            print("👋 Exiting... Thank you!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()