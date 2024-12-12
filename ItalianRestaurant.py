#Inheritence:
#"super()"
#in the child class's constructor, we call the `super()` function.
# this is the parent class's __init__ function.
from Restaurant import Restaurant;

class ItalianRestaurant(Restaurant):
    def __init__(self,name,rating,locations):
        super().__init__(name,"Italian",rating,locations)
    
    #ItalianRestaurant Methods
    #PastaTypes

    def pastaTypes(self):
        return ["Spaghetti","Lasagna"]