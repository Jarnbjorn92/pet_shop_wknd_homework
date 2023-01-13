# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(shop_name):
    return shop_name['name']

def get_total_cash(money_total):
    return money_total['admin']['total_cash']

def add_or_remove_cash(pet_shop, amount):
    pet_shop['admin']['total_cash'] += amount

def get_or_remove_cash(pet_shop, amount):
    pet_shop['admin']['total_cash'] -= amount


def get_pets_sold(pet_shop):
    return pet_shop['admin']['pets_sold']

def increase_pets_sold(pets_sold, amount):
    pets_sold['admin']['pets_sold'] += amount

def get_stock_count(pets):
    return len(pets['pets'])

def get_pets_by_breed(shop, breed):
    num_breed = []
    total = 0
    for pets in shop:
        if shop['pets'][total]['breed'] == breed:
            num_breed.append(pets)
            total += 1
            
    return num_breed

def find_pet_by_name(pet_shop, pet_name):
    for pets in pet_shop['pets']:
        if pets['name'] == pet_name:
            return pets

def remove_pet_by_name(pet_shop, pet_name):
    for pets in pet_shop['pets']:
        if pets['name'] == pet_name:
            pet_shop['pets'].remove(pets)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop['pets'].append(new_pet)

def get_customer_cash(customer):
    return customer['cash']

def remove_customer_cash(customer, cash):
    customer['cash'] -= cash

def get_customer_pet_count(customer):
    return len(customer['pets'])

def add_pet_to_customer(customer, new_pet):
    return customer['pets'].append(new_pet)




def customer_can_afford_pet(customer, pet):
    return customer['cash'] >= pet['price']

# def customer_can_afford_pet(customer, pet):
#     if customer['cash'] >= pet['price']:
#         return True
#     else:
#         return False

def sell_pet_to_customer(pet_shop, pet, customer):
    if pet in pet_shop['pets']:
        if customer_can_afford_pet(customer, pet):
            remove_customer_cash(customer, pet['price'])
            remove_pet_by_name(pet_shop, pet)
            add_pet_to_customer(customer, pet)
            pet_shop['admin']['total_cash'] += pet['price']
            pet_shop['admin']['pets_sold'] += 1

