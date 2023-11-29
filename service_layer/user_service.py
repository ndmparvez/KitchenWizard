import requests
# from flask import Flask, jsonify

class UserService:
    def connect_user(self, user_data, api_key):
        url = "https://api.spoonacular.com/users/connect"
        headers = {"Content-Type": "application/json"}
        params = {"apiKey": api_key}

        response = requests.post(url, headers=headers, params=params, json=user_data)

        if response.status_code == 200:
            data = response.json()
            print(data)
        else:
            return {"error": f"Request failed with status code {response.status_code}"}
    
    # Flask route for testing
# @app.route('/test-connect-user', methods=['GET'])
# def test_connect_user():
#     # Replace 'YOUR_API_KEY' with your actual Spoonacular API key
#     api_key = "YOUR_API_KEY"

#     # Sample user data
#     user_data = {
#         "username": "your user's name",
#         "firstName": "your user's first name",
#         "lastName": "your user's last name",
#         "email": "your user's email"
#     }

#     # Create UserService instance
#     user_service = UserService()

#     # Connect the user
#     response = user_service.connect_user(user_data, api_key)

#     # Return the response as JSON
#     return jsonify(response)

# if __name__ == "__main__":
#     # Run the Flask app for testing
#     app.run(debug=True)