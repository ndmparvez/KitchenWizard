# api/controllers/recipe_controller.py
from flask import Blueprint, jsonify
from service_layer.recipe_service import RecipeService

recipe_controller = Blueprint('recipe_controller', __name__)
recipe_service = RecipeService()

@recipe_controller.route('/recipes', methods=['GET'])
def get_recipes():
    query = 'milk'
    diet = 'Indian'
    api_key = '3d18ed4aab4647299471295f8f726c9a'
    recipes = recipe_service.get_recipes_from_api(query, diet, api_key)
    return jsonify(recipes)
