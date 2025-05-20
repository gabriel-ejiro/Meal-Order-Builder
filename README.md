# Meal-Order-Builder

 Objective:
 
Design a system that allows building a meal step by step using the Builder Design Pattern. The system should support different types of predefined meal sets (e.g., Kids Meal, Premium Meal) and enable flexible creation of new combinations in the future.

📘 Domain Story:

A fast-food restaurant wants to streamline its meal ordering process.
Customers should be able to select preconfigured meals or build custom ones from components: a main dish, a side dish, a drink, and a dessert.
The goal is to isolate the construction logic so that future changes (like adding Vegan Meals) don’t require modifying the existing logic of the meal creator.

📋 Functional Requirements:
- Allow building a meal in four parts: main dish, side, drink, dessert.

- Implement at least two predefined meal sets using the Builder Pattern.

- Enable printing of the complete meal once constructed.


🧱 Class Structure:

- Meal:	The final product

- MealBuilder:	Abstract builder interface

- KidsMealBuilder:	Concrete builder for kids meals

- PremiumMealBuilder:	Concrete builder for premium meals

- MealDirector:	Directs the step-by-step meal creation
