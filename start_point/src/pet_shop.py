# WRITE YOUR FUNCTIONS HERE

#function takes a pet shop dictionary as an argument and 
#returns the name of said pet shop 
def get_pet_shop_name(petshop_dictionary):
    return petshop_dictionary["name"]

#function takes a pet shop dictionary as an argument and
#returns the total cash of that petshop
def get_total_cash(petshop_dictionary):
    return petshop_dictionary["admin"]["total_cash"]

#function takes a pet shop dictionary and a number
#as an argument and adds the number passed to the the total 
#cash of the petshop dictionary. For losses write a 
#negative number. 
def add_or_remove_cash(petshop_dictionary, cash):
    petshop_dictionary["admin"]["total_cash"] += cash

#function takes a pet shop dictionary as an argument and 
#returns total number of pets sold
def get_pets_sold(petshop_dictionary):
    return petshop_dictionary["admin"]["pets_sold"]

#function takes in a petshop dictionary and a number as
#an argument and increases the total pets sold, in the
#pet shop dictionary, by that number. 
def increase_pets_sold(petshop_dictionary, pets_sold):
    petshop_dictionary["admin"]["pets_sold"] += pets_sold

#function takes in a petshop dictionary as a function
#and returns the total stock of pets 
def get_stock_count(petshop_dictionary):
    return len(petshop_dictionary["pets"])

#function takes in a petshop dictionary and pet breed 
#as an argument and returns the total number of pets
#in stock of said breed, as an int
def get_pets_by_breed(petshop_dictionary, breed):
    breed_list = []
    for b in petshop_dictionary["pets"]:
        if b["breed"] == breed:
            breed_list.append(b)
    return breed_list

#function takes in a petshop dictionary and pet name
#as an argument and returns a dictionary of the pet
#returns None if no pet is found 

def find_pet_by_name(petshop_dictionary, name):
    name_dict = {}
    for n in petshop_dictionary["pets"]:
        if n["name"] == name:
            name_dict["name"] = n["name"]
    if name_dict != {}:
        return name_dict
        

    
    





    
