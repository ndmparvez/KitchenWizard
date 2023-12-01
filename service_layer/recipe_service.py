import requests


class RecipeService:
    
    def get_recipes_from_api(self, query, diet, cuisine ,api_key):
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

        
        
    def get_recipes_instruction_api(self ,forceExtraction , analyze , includeNutrition , includeTaste  , apiKey):
        url = 'https://foodista.com/recipe/ZHK4KPB6/chocolate-crinkle-cookies'
        fullApiUrl = 'https://api.spoonacular.com/recipes/extract'
        params = {
            'url' : url,
            'forceExtraction' : forceExtraction,
            'analyze' : analyze,
            'includeNutrition' : includeNutrition,
            'includeTaste' : includeTaste,
            'apiKey' : apiKey
        }
    
        try:
            response = requests.get(fullApiUrl , params= params)
            if response.status_code == 200:
                # Parse the JSON response and return the instructions
                data = response.json()
                instructions = data.get('instructions')
                return instructions if instructions else "No instructions found in the response."
            else:
                return f"API request failed with status code {response.status_code}."
        except Exception as e:
            return f"Error: {str(e)}"
    
    def generate_response(self , response) :
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return {"error": f"API request failed with status code {response.status_code}", "response_data": response.text}