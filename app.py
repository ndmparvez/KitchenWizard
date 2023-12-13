from flask import Flask, jsonify , render_template, request, redirect, url_for
from flask_bcrypt import Bcrypt
import pymysql
import requests

app = Flask(__name__)
bcrypt = Bcrypt(app)
api_key = '3d18ed4aab4647299471295f8f726c9a'

# Replace these values with your MariaDB connection details
db_config = {
    "host": "database-1.cq27a1ilgnpq.us-east-1.rds.amazonaws.com",
    "user": "admin",
    "password": "Qmulsept2023",
    "database": "mydatabase",  # Specify the database name
}

def create_connection():
    return pymysql.connect(
        host=db_config["host"],
        user=db_config["user"],
        password=db_config["password"],
        database=db_config["database"],
        cursorclass=pymysql.cursors.DictCursor,
    )

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        try:
            data = request.get_json()
            name = data.get('Name')
            email = data.get('email')
            password = data.get('password')
            print(f"name : {name} \n email : {email} \n password : {password}")

            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            print(f"Hashed Password : {hashed_password}")
            with create_connection() as connection:
                with connection.cursor() as cursor:
                    # Insert values into the 'user' table
                    insert_query = "INSERT INTO user (name, email, password) VALUES (%s, %s, %s)"
                    #user_data = (name, email, password)
                    cursor.execute(insert_query, (name , email , hashed_password))
                    connection.commit()

        #return render_template('login.html')
            return jsonify({"success": True})
        except Exception as e:
            print("Error:", str(e))
            return jsonify({"success": False})
    return render_template('signup.html')                                                                                                                                                           
@app.route('/login', methods=['GET', 'POST'])
def login():
    login_error = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        with create_connection() as connection:
            with connection.cursor() as cursor:
                # Check if the user exists in the 'user' table
                select_query = "SELECT * FROM user WHERE email = %s"
                cursor.execute(select_query, (email,))
                user = cursor.fetchone()

        if user and bcrypt.check_password_hash(user['password'], password):
            return render_template('index.html')
        else:
            login_error = "Login failed. Invalid email or password."

    return render_template('login.html', login_error=login_error )
@app.route('/get_recipes', methods=['POST'])
def search_recipes():
    query = request.form.get('search')
    diet = request.form.get('select1')
    cuisine = request.form.get('select2')
    recipes = get_recipes_from_api(query, diet, cuisine, api_key)
    return jsonify(recipes)

def get_recipes_from_api(query, diet, cuisine ,api_key):
        api_url = 'https://api.spoonacular.com/recipes/complexSearch'
        params = {
            'query': query,
            'diet': diet,
            'cuisine' : cuisine,
            'apiKey': api_key
        }
        print(params)
        response = requests.get(api_url, params=params)

        if response.status_code == 200:
            data = response.json()
            print(data)
            return data
        else:
            return {"error": f"API request failed with status code {response.status_code}", "response_data": response.text}

if __name__ == '__main__':
    app.run(debug=True)
