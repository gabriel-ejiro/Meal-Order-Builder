
class Meal:
    def __init__(self):
        self.main = {}
        self.side = {}
        self.drink = {}
        self.dessert = {}

    def __str__(self):
        def format_part(part):
            if not part: return "None"
            return f"{part['item']} (₦{part['price']}, {part['calories']} cal)"

        return (
            f"Meal:\n"
            f"  Main: {format_part(self.main)}\n"
            f"  Side: {format_part(self.side)}\n"
            f"  Drink: {format_part(self.drink)}\n"
            f"  Dessert: {format_part(self.dessert)}"
        )
