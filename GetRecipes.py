import requests
import json

# Replace 'YOUR_API_KEY' with your actual Spoonacular API key
api_key = '3d18ed4aab4647299471295f8f726c9a'

# Define the API endpoint URL
api_url = 'https://api.spoonacular.com/recipes/complexSearch'

# Define the query parameters
params = {
    'query': 'milk,bread',
    'diet' : 'Indian',
    'apiKey': api_key
}

# Send a GET request to the API
response = requests.get(api_url, params=params)

# Check the response status code
if response.status_code == 200:
    # Response is successful (HTTP status code 200)
    data = response.json()  # Parse the JSON response
    formatted_data = json.dumps(data, indent=4)
    print("Response data:")
    print(formatted_data)
else:
    # Response status code indicates an error
    print(f"API request failed with status code {response.status_code}")
    print("Response data:")
    print(response.text)
