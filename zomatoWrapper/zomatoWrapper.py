import requests
import ast
import json


class Zomato:

    def __init__(self, user_key):
        """Define objects of type Zomato

        Parameters:
        api_key: API key to access https://developers.zomato.com/api/v2.1/

        """
        self.user_key = user_key
        self.base_url = "https://developers.zomato.com/api/v2.1/"
    

    
    def get_categories(self):
        """ This api provides you the list
        of categories of foods.
        
        Parameters:
        """        
        headers= {'Accept':'applicaiton/json', 'user-key': self.user_key}
        response = (requests.get(self.base_url + "categories", headers=headers).content).decode("utf-8")
        category_string = ast.literal_eval(response)
        
        categories = {}
        for category in category_string['categories']:
            categories.update({category['categories']['id']: category['categories']['name']})

        # print(categories)

        return categories
    

    
