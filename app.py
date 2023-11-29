from flask import Flask , render_template
from api.controllers.recipe_controller import recipe_controller
from api.controllers.user_controller import user_controller

app = Flask(__name__)
app.register_blueprint(recipe_controller)
app.register_blueprint(user_controller)

# @app.route('/')
# def helloWorld() :
#     return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
