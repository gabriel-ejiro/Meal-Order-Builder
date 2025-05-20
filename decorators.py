
class ExtraCheese(MealComponentDecorator):
    def add(self):
        item = self.component.copy()
        item['item'] += " + Extra Cheese"
        item['price'] += 200
        item['calories'] += 100
        return item

class HotSauce(MealComponentDecorator):
    def add(self):
        item = self.component.copy()
        item['item'] += " + Hot Sauce"
        item['price'] += 100
        item['calories'] += 20
        return item


# Cell 12: Decorator in action
print("=== Add-ons Example ===")
premium_builder = PremiumMealBuilder()
director = MealDirector(premium_builder)
meal = director.construct_meal()

# Add extra cheese to main
meal.main = ExtraCheese(meal.main).add()

# Add hot sauce to side
meal.side = HotSauce(meal.side).add()

print(meal)


