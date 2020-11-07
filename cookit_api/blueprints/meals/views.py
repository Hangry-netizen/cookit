from flask import Blueprint, jsonify, request
from models.meal import Meal

meals_api_blueprint = Blueprint('meals_api',
                             __name__)

@meals_api_blueprint.route('/', methods=['GET'])
def index():
    meals = Meal.select()
    return jsonify([{
      "id": meal.id,
      "name": meal.name,
      "prep_time": meal.prep_time,
      "cookware": meal.cookware,
      "url": meal.url
      } for meal in meals])


@meals_api_blueprint.route('/', methods=['POST'])
def create():
    data = request.json

    name = data.get('name')
    ingredients = data.get('ingredients')
    prep_time = data.get('prep_time')
    cookware = data.get('cookware')
    url = data.get('url')

    if name and ingredients and prep_time and url:
        meal = Meal(
            name = name,
            ingredients = ingredients,
            prep_time = prep_time,
            cookware = cookware,
            url = url
        )
        if meal.save():
            return jsonify({
                "message": "Successfully created the meal!",
                "status": "success",
                "meal": {
                    "id": meal.id,
                    "name": meal.name
                }
            })
        elif meal.errors != 0:
            return jsonify({
                "message": [error for error in meal.errors],
                "status": "failed"
            })
    else:
        return jsonify({
            "message": "All fields are required!",
            "status": "failed"
        })
