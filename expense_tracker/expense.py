class Expense:

    def __init__(self, name, amount, category, date):
        self.name = name
        self.amount = amount
        self.category = category
        self.date = date

    def display(self):

        print(
            f"Name: {self.name} | "
            f"Amount: ₹{self.amount:.2f} | "
            f"Category: {self.category} | "
            f"Date: {self.date}"
        )