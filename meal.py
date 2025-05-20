class Meal:
    def __init__(self):
        self.main = None
        self.side = None
        self.drink = None
        self.dessert = None

    def __str__(self):
        return (
            f"Meal:\n"
            f"  Main: {self.main}\n"
            f"  Side: {self.side}\n"
            f"  Drink: {self.drink}\n"
            f"  Dessert: {self.dessert}"
        )
