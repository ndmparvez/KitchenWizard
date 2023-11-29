from flask import Blueprint, jsonify
from service_layer.recipe_service import RecipeService

recipe_controller = Blueprint('recipe_controller', __name__)
recipe_service = RecipeService()
api_key = '3d18ed4aab4647299471295f8f726c9a'

@recipe_controller.route('/recipes', methods=['GET'])
def get_recipes():
    query = 'milk , eggs'
    diet = 'Indian'
    recipes = recipe_service.get_recipes_from_api(query, diet, api_key)
    return jsonify(recipes)

@recipe_controller.route('/recipeInst', methods = ['GET'])
def get_recipe_instructions():

    forceExtraction = 'true'
    analyze = 'false'
    includeNutrition = 'false'
    includeTaste = 'false'
    recipeInstructions = recipe_service.get_recipes_instruction_api(forceExtraction , analyze , includeNutrition , includeTaste,api_key)
    return jsonify(recipeInstructions)
