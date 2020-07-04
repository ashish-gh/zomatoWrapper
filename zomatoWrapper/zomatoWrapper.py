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

        Returns:
            categories: ''dict''
                key value pair of categorie id and name
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
        of provided city name.

        Parameters:
            city_name: ''str'
                name for specific city
        
        Return:
            None
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

        self.is_key_valid(city_string)
        
        # checking if passed city name is valid
        try:
            if (len(city_string['location_suggestions']) == 0):
                raise ValueError
            else:
                for city in city_string['location_suggestions']:
                    return city['id']

        except ValueError:
            print("city name is inappropriate.")

        
    def get_cityName(self, city_id):
        """This api provides city details
        of provided city id.

        Parameters:
            city_id : ''int'' 
                city id for specific city 

        Return
            city_name: ''str''
                name of city id
        """

        city_id = str(city_id)
            
        # checking if city id is numeric
        try:
            if city_id.isnumeric() == False:
                raise ValueError
        except ValueError:
            print("city id is invalid.")

        headers= {'Accept':'applicaiton/json', 'user-key': self.user_key}        
        response = (requests.get(self.base_url + "cities?city_ids="+str(city_id), headers=headers).content).decode("utf-8")
        city_string = json.loads(response)

        # checking user-key
        self.is_key_valid(city_string)

        # checking if passed city id is valid
        try:
            if (len(city_string['location_suggestions']) == 0):
                raise ValueError
            else:
                for city in city_string['location_suggestions']:
                    return city['name']
        except ValueError:
            print("city id is inappropriate.")



    def is_key_valid(self, response_string):
        """
        """
        try:
            if 'code' in response_string:
                if response_string['code'] == 403:
                    raise ValueError
                            
        except ValueError:
            print("user key is not valid")
        
            
        





    
