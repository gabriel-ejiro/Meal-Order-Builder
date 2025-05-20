
class KidsMealBuilder(MealBuilder):
    def add_main(self):
        self.meal.main = {"item": "Mini Burger", "price": 1000, "calories": 350}

    def add_side(self):
        self.meal.side = {"item": "Small Fries", "price": 500, "calories": 250}

    def add_drink(self):
        self.meal.drink = {"item": "Juice Box", "price": 300, "calories": 100}

    def add_dessert(self):
        self.meal.dessert = {"item": "Mini Ice Cream", "price": 400, "calories": 180}


class PremiumMealBuilder(MealBuilder):
    def add_main(self):
        self.meal.main = {"item": "Double Cheeseburger", "price": 2500, "calories": 700}

    def add_side(self):
        self.meal.side = {"item": "Large Fries", "price": 1000, "calories": 500}

    def add_drink(self):
        self.meal.drink = {"item": "Coca-Cola", "price": 600, "calories": 180}

    def add_dessert(self):
        self.meal.dessert = {"item": "Cheesecake", "price": 1200, "calories": 450}
