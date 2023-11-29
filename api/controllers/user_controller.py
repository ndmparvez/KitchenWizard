from flask import Blueprint, jsonify , request
from service_layer.user_service import UserService  

user_controller = Blueprint('user_controller', __name__)
user_service = UserService()
api_key = '3d18ed4aab4647299471295f8f726c9a'

@user_controller.route('/connect-user', methods=['POST'])
def connect_user():
    
    user_data = request.get_json()

    if 'username' not in user_data or 'firstName' not in user_data or 'lastName' not in user_data or 'email' not in user_data:
        return jsonify({"error": "Invalid JSON data. Required fields: username, firstName, lastName, email"}), 400
    
    result = user_service.connect_user(user_data, api_key=api_key)
    return jsonify({"message": "User connected successfully"})

