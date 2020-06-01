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


        return categories
    

    def get_cityID(self, city_name):
        """This api provides city details
        of provided city id.

        Parameters:
        """
        # converting to lower
        city_name = city_name.lower()

        # splitting city name
        city_name = city_name.split(' ')

        # joining city name to match url 
        city_name = '%20'.join(city_name)
        

        headers= {'Accept':'applicaiton/json', 'user-key': self.user_key}        
        response = (requests.get(self.base_url + "cities?q="+str(city_name), headers=headers).content).decode("utf-8")

        city_string = json.loads(response)
        
        # checking if passed city name is valid
        try:
            if (len(city_string['location_suggestions']) == 0):
                raise ValueError
            else:
                for city in city_string:
                    return city['id']

        except ValueError:
            print("city name is inappropriate.")




    
