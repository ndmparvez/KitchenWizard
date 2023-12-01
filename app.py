from flask import Flask , render_template , request , jsonify
from service_layer.recipe_service import RecipeService


app = Flask(__name__)

recipe_service = RecipeService()
api_key = '3d18ed4aab4647299471295f8f726c9a'

@app.route('/')
def render_index() :
    return render_template('index.html')

@app.route('/get_recipes', methods=['POST'])
def search_recipes():
    query = request.form.get('search')
    diet = request.form.get('select1')
    cuisine = request.form.get('select2')
    recipes = recipe_service.get_recipes_from_api(query, diet, cuisine, api_key)
    return jsonify(recipes)

if __name__ == '__main__':
    app.run(debug=True)
