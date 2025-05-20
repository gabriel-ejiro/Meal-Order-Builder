from MealBuilder import MealBuilder
from Meal import Meal

class CustomMealBuilder(MealBuilder):
    def add_main_dish(self):
        self.meal.main_dish = input("Choose main dish: ")

    def add_side(self):
        self.meal.side = input("Choose side: ")

    def add_drink(self):
        self.meal.drink = input("Choose drink: ")

    def add_dessert(self):
        self.meal.dessert = input("Choose dessert: ")
