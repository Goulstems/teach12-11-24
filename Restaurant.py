class Restaurant:
    def __init__(self,name,type,rating,locations):
       self.restaurantName = name
       self.restaurantType = type
       self.restaurantRating = rating
       self.restaurantLocations = locations

    def describe_restaurant(self):       #Method 1
        print(self.restaurantName)
        print(self.restaurantType)
        print(self.restaurantRating)
        print(self.restaurantLocations)

#More methods


#Inheritence
    #ItalianRestaurant super() --> Restaurant.__init__()
    #5StarRestaurant