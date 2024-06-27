import json
import os

class ExpenseTracker:
    def __init__(self, filename):
        self.filename = filename
        self.expenses = self.load_expenses()

    def load_expenses(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        else:
            return {}

    def save_expenses(self):
        with open(self.filename, 'w') as f:
            json.dump(self.expenses, f)

    def add_expense(self, date, category, amount):
        if date not in self.expenses:
            self.expenses[date] = {}
        if category not in self.expenses[date]:
            self.expenses[date][category] = 0
        self.expenses[date][category] += amount
        self.save_expenses()

    def get_expenses(self, date=None, category=None):
        if date and category:
            return self.expenses.get(date, {}).get(category, 0)
        elif date:
            return self.expenses.get(date, {})
        elif category:
            expenses = {}
            for date, categories in self.expenses.items():
                if category in categories:
                    expenses[date] = categories[category]
            return expenses
        else:
            return self.expenses

    def get_monthly_summary(self, year, month):
        summary = {}
        for date, categories in self.expenses.items():
            if date.startswith(f"{year}-{month:02}-"):
                for category, amount in categories.items():
                    if category not in summary:
                        summary[category] = 0
                    summary[category] += amount
        return summary

    def get_category_wise_expenditure(self):
        expenditure = {}
        for categories in self.expenses.values():
            for category, amount in categories.items():
                if category not in expenditure:
                    expenditure[category] = 0
                expenditure[category] += amount
        return expenditure

def main():
    filename = 'expenses.json'
    tracker = ExpenseTracker(filename)

    while True:
        print("1. Add Expense")
        print("2. Get Expenses")
        print("3. Get Monthly Summary")
        print("4. Get Category-wise Expenditure")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            tracker.add_expense(date, category, amount)
        elif choice == "2":
            date = input("Enter date (YYYY-MM-DD) or leave blank for all: ")
            category = input("Enter category or leave blank for all: ")
            if date and category:
                expenses = tracker.get_expenses(date, category)
            elif date:
                expenses = tracker.get_expenses(date)
            elif category:
                expenses = tracker.get_expenses(category=category)
            else:
                expenses = tracker.get_expenses()
            print(expenses)
        elif choice == "3":
            year = int(input("Enter year: "))
            month = int(input("Enter month: "))
            summary = tracker.get_monthly_summary(year, month)
            print(summary)
        elif choice == "4":
            expenditure = tracker.get_category_wise_expenditure()
            print(expenditure)
        elif choice == "5":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()