class ExpenseTracker:

    def __init__(self):
        self.expenses = []

    # Add an expense
    def add_expense(self, expense):

        self.expenses.append(expense)

        print("\nExpense added successfully!")

    # View all expenses
    def view_expenses(self):

        if len(self.expenses) == 0:
            print("\nNo expenses available.")
            return

        print("\n========== ALL EXPENSES ==========")

        for i in range(len(self.expenses)):

            print(f"\nExpense {i + 1}")

            self.expenses[i].display()

    # Calculate total expenses
    def calculate_total(self):

        total = 0

        for expense in self.expenses:
            total += expense.amount

        return total

    # Find highest expense
    def highest_expense(self):

        if len(self.expenses) == 0:
            return None

        highest = self.expenses[0]

        for expense in self.expenses:

            if expense.amount > highest.amount:
                highest = expense

        return highest

    # Find lowest expense
    def lowest_expense(self):

        if len(self.expenses) == 0:
            return None

        lowest = self.expenses[0]

        for expense in self.expenses:

            if expense.amount < lowest.amount:
                lowest = expense

        return lowest

    # Category-wise analysis
    def category_analysis(self):

        if len(self.expenses) == 0:
            print("\nNo expenses available.")
            return

        categories = {}

        for expense in self.expenses:

            if expense.category in categories:
                categories[expense.category] += expense.amount

            else:
                categories[expense.category] = expense.amount

        print("\n========== CATEGORY-WISE SPENDING ==========")

        for category in categories:

            print(
                f"{category}: "
                f"₹{categories[category]:.2f}"
            )

    # Complete expense analysis
    def analyze_expenses(self):

        if len(self.expenses) == 0:

            print("\nNo expenses available for analysis.")
            return

        total = self.calculate_total()

        average = total / len(self.expenses)

        highest = self.highest_expense()

        lowest = self.lowest_expense()

        print("\n========== EXPENSE ANALYSIS ==========")

        print(f"Total Spending: ₹{total:.2f}")

        print(
            f"Number of Expenses: "
            f"{len(self.expenses)}"
        )

        print(
            f"Average Expense: "
            f"₹{average:.2f}"
        )

        print("\nHighest Expense:")

        highest.display()

        print("\nLowest Expense:")

        lowest.display()

        self.category_analysis()

    # Search expense
    def search_expense(self, keyword):

        found = False

        print("\n========== SEARCH RESULTS ==========")

        for expense in self.expenses:

            if keyword.lower() in expense.name.lower():

                expense.display()

                found = True

        if not found:

            print("No matching expense found.")

    # Delete expense
    def delete_expense(self, number):

        if number < 1 or number > len(self.expenses):

            print("\nInvalid expense number.")

            return

        deleted = self.expenses.pop(number - 1)

        print(
            f"\nExpense '{deleted.name}' "
            f"deleted successfully!"
        )