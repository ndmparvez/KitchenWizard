import requests

class RecipeService:
    #Need to be encrypted
    api_key = ''
    def get_recipes_from_api(self, query, diet, api_key):
        api_url = 'https://api.spoonacular.com/recipes/complexSearch'
        params = {
            'query': query,
            'diet': diet,
            'apiKey': api_key
        }

        response = requests.get(api_url, params=params)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return {"error": f"API request failed with status code {response.status_code}", "response_data": response.text}
