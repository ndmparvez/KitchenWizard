from flask import Flask , render_template
from api.controllers.recipe_controller import recipe_controller

app = Flask(__name__)
app.register_blueprint(recipe_controller)

@app.route('/')
def helloWorld() :
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
