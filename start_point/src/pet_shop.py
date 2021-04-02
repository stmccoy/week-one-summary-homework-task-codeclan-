# WRITE YOUR FUNCTIONS HERE

#function takes a petshop dictionary as an argument and 
#returns the name of said petshop  
def get_pet_shop_name(petshop_dictionary):
    return petshop_dictionary["name"]

#function takes a petshop dictionary as an argument and
#returns the total cash of that petshop
def get_total_cash(petshop_dictionary):
    return petshop_dictionary["admin"]["total_cash"]

#function takes a petshop dictionary and a number
#as an argument and adds the number passed to the total 
#cash of the petshop dictionary. For losses write a 
#negative number. 
def add_or_remove_cash(petshop_dictionary, cash):
    petshop_dictionary["admin"]["total_cash"] += cash

#function takes a petshop dictionary as an argument and 
#returns total number of pets sold
def get_pets_sold(petshop_dictionary):
    return petshop_dictionary["admin"]["pets_sold"]

#function takes a petshop dictionary and a number as
#an argument and increases the total pets sold, in the
#petshop dictionary, by that number. 
def increase_pets_sold(petshop_dictionary, pets_sold):
    petshop_dictionary["admin"]["pets_sold"] += pets_sold

#function takes a petshop dictionary as an arugment
#and returns the total stock of pets 
def get_stock_count(petshop_dictionary):
    return len(petshop_dictionary["pets"])

#function takes a petshop dictionary and pet breed 
#as an argument and returns the total number of pets
#in stock of said breed, as an int
def get_pets_by_breed(petshop_dictionary, breed):
    breed_list = []
    for b in petshop_dictionary["pets"]:
        if b["breed"] == breed:
            breed_list.append(b)
    return breed_list

#function takes a petshop dictionary and pet name
#as an argument and returns the pet dictionary associated with
#the pet name. Function returns None if pet name is not found 
def find_pet_by_name(petshop_dictionary, name):
    name_dict = {}
    for n in petshop_dictionary["pets"]:
        if n["name"] == name:
            name_dict["name"] = n["name"]
    if name_dict != {}:
        return name_dict

#function takes a petshop dictionary and pet name
#as an argument and removes said pet name from the nested list of
#pet dictionaries contained within the pet shop dictionary. 
# Returns None if pet name not found
def remove_pet_by_name(petshop_dictionary, name):
    length_of_list_for_indexing = (len(petshop_dictionary["pets"])) - 1
    for i in range(length_of_list_for_indexing):
        if petshop_dictionary["pets"][i]["name"] == name:
            del petshop_dictionary["pets"][i]

#function takes a petshop dictionary and new pet dictionary 
#as an argument and adds the new pet dictionary to the nested 
#list of pet dictionaries contained within the petshop dictionary
def add_pet_to_stock(petshop_dictionary, new_pet):
    petshop_dictionary["pets"].append(new_pet)

#function takes a customer dictionary and returns the cash element
def get_customer_cash(customer_dictionary):
    return customer_dictionary["cash"]

#function takes a customer dictionary and subtracts the amount 
#passed as the cash_removed argument from the cash element of 
#said customer dictionary
def remove_customer_cash(customer_dictionary, cash_removed):
    customer_dictionary["cash"] -= cash_removed

#function takes a customer dictionary and returns the pet count
#for said customer
def get_customer_pet_count(customer_dictionary):
    return len(customer_dictionary["pets"])

#function takes a customer dictionary and a new pet argument 
#and adds the new pet to the customer dictionary pet list
def add_pet_to_customer(customer_dictionary, new_pet):
    customer_dictionary["pets"].append(new_pet)



    
    





    
