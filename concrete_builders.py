class KidsMealBuilder(MealBuilder):
    def add_main(self):
        self.meal.main = "Mini Burger"

    def add_side(self):
        self.meal.side = "Small Fries"

    def add_drink(self):
        self.meal.drink = "Juice Box"

    def add_dessert(self):
        self.meal.dessert = "Mini Ice Cream"

class PremiumMealBuilder(MealBuilder):
    def add_main(self):
        self.meal.main = "Double Cheeseburger"

    def add_side(self):
        self.meal.side = "Large Fries"

    def add_drink(self):
        self.meal.drink = "Coca-Cola"

    def add_dessert(self):
        self.meal.dessert = "Cheesecake"
