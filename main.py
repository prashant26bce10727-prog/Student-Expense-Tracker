from expense_tracker.expense import Expense
from expense_tracker.tracker import ExpenseTracker


def add_expense(tracker):

    print("\n========== ADD EXPENSE ==========")

    name = input("Enter expense name: ").strip()

    while name == "":
        print("Expense name cannot be empty.")
        name = input("Enter expense name: ").strip()

    while True:
        try:
            amount = float(input("Enter amount: ₹"))

            if amount <= 0:
                print("Amount must be greater than 0.")
            else:
                break

        except ValueError:
            print("Please enter a valid amount.")

    print("\nSelect Category")
    print("1. Food")
    print("2. Travel")
    print("3. Education")
    print("4. Shopping")
    print("5. Entertainment")
    print("6. Other")

    while True:

        category_choice = input("Enter choice (1-6): ")

        if category_choice == "1":
            category = "Food"
            break

        elif category_choice == "2":
            category = "Travel"
            break

        elif category_choice == "3":
            category = "Education"
            break

        elif category_choice == "4":
            category = "Shopping"
            break

        elif category_choice == "5":
            category = "Entertainment"
            break

        elif category_choice == "6":
            category = "Other"
            break

        else:
            print("Invalid choice. Please select 1-6.")

    date = input("Enter date (DD/MM/YYYY): ").strip()

    while date == "":
        print("Date cannot be empty.")
        date = input("Enter date (DD/MM/YYYY): ").strip()

    expense = Expense(name, amount, category, date)

    tracker.add_expense(expense)


def delete_expense(tracker):

    if len(tracker.expenses) == 0:
        print("\nNo expenses available.")
        return

    tracker.view_expenses()

    while True:
        try:
            number = int(
                input("\nEnter expense number to delete: ")
            )

            if 1 <= number <= len(tracker.expenses):
                tracker.delete_expense(number)
                break
            else:
                print("Invalid expense number.")

        except ValueError:
            print("Please enter a valid number.")


def search_expense(tracker):

    if len(tracker.expenses) == 0:
        print("\nNo expenses available.")
        return

    keyword = input(
        "\nEnter expense name to search: "
    ).strip()

    if keyword == "":
        print("Search cannot be empty.")
        return

    tracker.search_expense(keyword)


def main():

    tracker = ExpenseTracker()

    while True:

        print("\n")
        print("=" * 50)
        print("       STUDENT EXPENSE TRACKER")
        print("=" * 50)

        print("\n1. Add Expense")
        print("2. View All Expenses")
        print("3. Expense Analysis")
        print("4. Search Expense")
        print("5. Delete Expense")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_expense(tracker)

        elif choice == "2":
            tracker.view_expenses()

        elif choice == "3":
            tracker.analyze_expenses()

        elif choice == "4":
            search_expense(tracker)

        elif choice == "5":
            delete_expense(tracker)

        elif choice == "6":
            print("\nThank you for using Student Expense Tracker!")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()