class MealDirector:
    def __init__(self, builder: MealBuilder):
        self.builder = builder

    def construct_meal(self):
        self.builder.add_main()
        self.builder.add_side()
        self.builder.add_drink()
        self.builder.add_dessert()
        return self.builder.get_meal()
