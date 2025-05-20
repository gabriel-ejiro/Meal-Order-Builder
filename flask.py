
import nest_asyncio
nest_asyncio.apply()

from flask import Flask, request, jsonify
from threading import Thread

app = Flask(__name__)


# Cell 14: Helper function to jsonify Meal
def meal_to_dict(meal):
    return {
        "main": meal.main,
        "side": meal.side,
        "drink": meal.drink,
        "dessert": meal.dessert,
        "total_price": sum(part["price"] for part in [meal.main, meal.side, meal.drink, meal.dessert]),
        "total_calories": sum(part["calories"] for part in [meal.main, meal.side, meal.drink, meal.dessert])
    }

