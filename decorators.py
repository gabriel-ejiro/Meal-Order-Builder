
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
