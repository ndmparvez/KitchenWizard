from flask import Flask
from api.controllers.recipe_controller import recipe_controller

app = Flask(__name__)
app.register_blueprint(recipe_controller)

if __name__ == '__main__':
    app.run(debug=True)
