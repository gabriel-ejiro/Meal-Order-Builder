from abc import ABC, abstractmethod

class MealBuilder(ABC):
    def __init__(self):
        self.meal = Meal()

    @abstractmethod
    def add_main(self):
        pass

    @abstractmethod
    def add_side(self):
        pass

    @abstractmethod
    def add_drink(self):
        pass

    @abstractmethod
    def add_dessert(self):
        pass

    def get_meal(self):
        return self.meal
