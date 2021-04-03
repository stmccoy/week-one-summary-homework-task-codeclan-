import pdb
# WRITE YOUR FUNCTIONS HERE

#function takes a petshop dictionary as an argument and 
#returns the "name" value of said petshop dictionary  
def get_pet_shop_name(petshop_dictionary):
    return petshop_dictionary["name"]

#function takes a petshop dictionary as an argument and
#returns the "total_cash" value of said petshop dictionary
def get_total_cash(petshop_dictionary):
    return petshop_dictionary["admin"]["total_cash"]

#function takes a petshop dictionary and a number as an argument and adds 
#the number passed to the ["admin"]["total_cash"] value of the petshop dictionary.
#For losses pass a negative number to the function. 
def add_or_remove_cash(petshop_dictionary, cash):
    petshop_dictionary["admin"]["total_cash"] += cash

#function takes a petshop dictionary as an argument and returns the
#["admin"]["pets_sold"] value of said dictionary
def get_pets_sold(petshop_dictionary):
    return petshop_dictionary["admin"]["pets_sold"]

#function takes a petshop dictionary and a number as arguments and increases 
#the ["admin"]["pets_sold"] value, in the petshop dictionary, by that number. 
def increase_pets_sold(petshop_dictionary, pets_sold):
    petshop_dictionary["admin"]["pets_sold"] += pets_sold

#function takes a petshop dictionary as an arugment and returns the number of 
#pet dictionaries contained within the "pets" value. This value takes the form 
#of a list, so the total pets is simply the length of that list
def get_stock_count(petshop_dictionary):
    return len(petshop_dictionary["pets"])

#function takes a petshop dictionary and pet breed as an argument and returns 
#the total number of pets of said breed from within the "pets", nested list, 
#value, within the petshop dictionary.
def get_pets_by_breed(petshop_dictionary, breed):
    breed_list = []
    for b in petshop_dictionary["pets"]:
        if b["breed"] == breed:
            breed_list.append(b)
    return breed_list

#function takes a petshop dictionary and pet name as an argument and returns the 
#pet dictionary associated with the pet name, from the "pets", nested list, value,
#within the petshop dictionary. Function returns None if no pet name is found within
#the "pets", nested list, value.
def find_pet_by_name(petshop_dictionary, name):
    name_dict = {}
    for n in petshop_dictionary["pets"]:
        if n["name"] == name:
            name_dict["name"] = n["name"]
            name_dict["pet_type"] = n["pet_type"]
            name_dict["breed"] = n["breed"]
            name_dict["price"] = n["price"]
    if name_dict != {}:
        return name_dict


#function takes a petshop dictionary and pet name as an argument and removes said 
#pet name from the pet's, nested list, value contained within the pet shop dictionary. 
#Returns None if pet name not found with the "pet's", nested list, value
def remove_pet_by_name(petshop_dictionary, name):
    length_of_list_for_indexing = (len(petshop_dictionary["pets"])) - 1
    for i in range(length_of_list_for_indexing):
        if petshop_dictionary["pets"][i]["name"] == name:
            del petshop_dictionary["pets"][i]

#function takes a petshop dictionary and new pet dictionary as an argument and adds 
#the new pet dictionary to the "pets", nested list, value contained within the petshop 
#dictionary
def add_pet_to_stock(petshop_dictionary, new_pet):
    petshop_dictionary["pets"].append(new_pet)

#function takes a customer dictionary and returns the "cash" value
def get_customer_cash(customer_dictionary):
    return customer_dictionary["cash"]

#function takes a customer dictionary and number and subtracts the  
#given number from the "cash" value of the customer dictionary
def remove_customer_cash(customer_dictionary, cash_removed):
    customer_dictionary["cash"] -= cash_removed

#function takes a customer dictionary and returns the "pets"
#value for said customer dictionary. The "pets" value takes the form of 
#a nested list contained within the customer dictionary, so the 
#pet count is simply the length of that list. 
def get_customer_pet_count(customer_dictionary):
    return len(customer_dictionary["pets"])

#function takes a customer dictionary and a pet dictionary
#and adds the pet dictionary to the "pets", nested list, value
#contained within the customer dictionary.
def add_pet_to_customer(customer_dictionary, new_pet):
    customer_dictionary["pets"].append(new_pet)

#function takes a customer and pet dictionary and compares the customer 
#dictionary "cash" value with the pet dictionary "price" value. If the 
#customer dictionary cash value is >= to the pet dictionary "price" value
#then the function returns True. Else the function returns False. 
def customer_can_afford_pet(customer_dictionary, petshop_dictionary):
    if customer_dictionary["cash"] >= petshop_dictionary["price"]:
        return True
    return False

#function takes in a petshop dictionary, a pet dictionary and a customer 
#dictionary.
# 
#The function first checks whether pet dictionary exists, and it does this
#by checking if the value is a dictionary or None type. If the value is a None 
#type then the function returns False.
# 
#If the pet dictionary exists then the the function runs the "customer_can_afford_pet()" 
#function descibed above to see whether the customer can afford the pet being suggested. 
#If customer cannot afford the pet then the function returns None.
# 
#else, the function adds the pet dictionary to the customer dictionary "pets", nested
#list, value. It then substracts the pet dictionary "price" value from the customer
#dictionary "cash"" value, and adds said value to the ["admin"]["total_cash"] value
#contained within the petshop dictionary. 
# 
#Finally it increases the ["admin"]["pets_sold"] value of the petshop dictionary by
#1 and deletes the pet dictionary from the "pets", nested list, value in the petshop 
#dictionary.
def sell_pet_to_customer(petshop_dictionary, pet_dictionary, customer_dictionary):
    if pet_dictionary is None:
        return False   
    elif customer_can_afford_pet(customer_dictionary, pet_dictionary):
        lst_index_position_for_pet = petshop_dictionary["pets"].index(pet_dictionary)
        customer_dictionary["pets"].append(petshop_dictionary["pets"][lst_index_position_for_pet])
        customer_dictionary["cash"] -= pet_dictionary["price"]
        petshop_dictionary["admin"]["total_cash"] += pet_dictionary["price"]
        petshop_dictionary["admin"]["pets_sold"] += 1
        del petshop_dictionary["pets"][lst_index_position_for_pet]
        

            
        

    
    





    
