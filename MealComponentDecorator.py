class MealComponentDecorator:
    def __init__(self, component):
        self.component = component

    def add(self):
        return self.component 
