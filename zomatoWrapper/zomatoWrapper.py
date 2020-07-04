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
    

    
    def getCategories(self):
        """ This api provides you the list
        of categories of foods.
        
        Parameters:

        Returns:
            categories: ''dict''
                key value pair of categorie id and name
        """        
        headers= {'Accept':'applicaiton/json', 'user-key': self.user_key}
        response = (requests.get(self.base_url + "categories", headers=headers).content).decode("utf-8")
        categoryString = ast.literal_eval(response)
        
        categories = {}
        for category in categoryString['categories']:
            categories.update({category['categories']['id']: category['categories']['name']})

        return categories
    


    def getCityID(self, cityName):
        """This api provides city details
        of provided city name.

        Parameters:
            cityName: ''str'
                name for specific city
        
        Return:
            cityId : ''int''
                unique cityId 
        """
        # converting to lower
        cityName = cityName.lower()

        # splitting city name
        cityName = cityName.split(' ')

        # joining city name to match url 
        cityName = '%20'.join(cityName)
        
        headers= {'Accept':'applicaiton/json', 'user-key': self.user_key}        
        response = (requests.get(self.base_url + "cities?q="+str(cityName), headers=headers).content).decode("utf-8")
        cityString = json.loads(response)

        self.isKeyValid(cityString)
        
        # checking if passed city name is valid
        try:
            if (len(cityString['location_suggestions']) == 0):
                raise ValueError
            else:
                for city in cityString['location_suggestions']:
                    return city['id']

        except ValueError:
            print("city name is inappropriate.")

        
    def getCityName(self, cityId):
        """This api provides city details
        of provided city id.

        Parameters:
            cityId : ''int'' 
                city id for specific city 

        Return
            city_name: ''str''
                name of city id
        """

        # checking if city id is numeric
        self.checkIsNumeric(cityId)

        cityId = str(cityId)
                    
        headers= {'Accept':'applicaiton/json', 'user-key': self.user_key}        
        response = (requests.get(self.base_url + "cities?city_ids="+str(cityId), headers=headers).content).decode("utf-8")
        cityString = json.loads(response)

        # checking user-key
        self.isKeyValid(cityString)

        # checking if passed city id is valid
        try:
            if (len(cityString['location_suggestions']) == 0):
                raise ValueError
            else:
                for city in cityString['location_suggestions']:
                    return city['name']
        except ValueError:
            print("city id is inappropriate.")

    def getCuisines(self, cityId):
        """This function returns list of cuisines 
        of restaurant for specific city.
        
        Parameters
            cityId: ''int''
                city id for restaurant

        Returns
            cuisines : ''list''
                list of cuisines 
        """
        
        # checking if cityId is valid or not
        self.checkIsNumeric(cityId)

        cityId = str(cityId)

        headers = {'Accept':'application/json', 'user-key': self.user_key}
        response = (requests.get(self.base_url+ "cuisines?city_id=" + str(cityId), headers=headers).content).decode("utf-8")
        cusinesString = json.loads(response)
        
        # checking status of request
        self.checkBadStatus(cusinesString)

        # checking if value for provided city is there or not
        self.checkCuisineForCity(cusinesString, cityId)

        cuisines = {}

        for cuisine in cusinesString["cuisines"]:
            cuisines.update({cuisine["cuisine"]["cuisine_id"] : cuisine["cuisine"]["cuisine_name"]})
        
        return cuisines
        
    def isKeyValid(self, responseString):
        """
        This function is used to check if API keyis valid or not
        
        Parameter
            responseString: ''dict''
                dictonary to hold reponse from API request
        
        Return 
            None
        """
        try:
            if 'code' in responseString:
                if responseString['code'] == 403:
                    raise ValueError 
                            
        except ValueError:
            print("user key is not valid")
    
           
    def checkBadStatus(self, responseString):
        """
        This function is used to check if data for given request exists or not.
        
        Parameter
            responseString: ''dict''
                dictonary to hold reponse from API request
        
        Return 
            None
        """
        try:
            if 'code' in responseString:
                if responseString['code'] == 400:
                    raise ValueError
        except ValueError:
            print("No data found")
            
        
    def checkIsNumeric(self, value):
        """        
        This function is used to check if API keyis valid or not
        
        Parameter
            value: ''int/str/boolean'' 
                input value from user
        
        Return 
            None
        """
        try:
            if isinstance(value, str):
                raise ValueError
        except ValueError:
            print("city id is invalid.")


    def checkCuisineForCity(self, responseString, cityId):
        """
        This function is used to check cuisines for specific city exists or not
        
        Parameter
            responseString: ''dict''
                dictonary to hold reponse from API request
            cityId: ''int''
                unique city id for city
        
        Return 
            None
        """
        try:
            if len(responseString["cuisines"]) == 0:
                raise ValueError            
        except ValueError:
            print("no data for {}".format(cityId))
            
        





    
