# TO-DO APP DEVELOPMENT USING BASIC CONSEPTS 

import time

product_details = {}

def add_data():
    id_number = int(input("Enter product id: "))
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    print("Adding data...")
    time.sleep(2)
    product_details[id_number] = {"name" : name, "price" : price}

    print("Data added successefully")

def delete_data():
    id_number = int(input("Enter product id: "))
    if id_number in product_details:
        del product_details[id_number]
        print("Product deleted")
    else:
        print("Please enter the valid product id")

def update_data():
    id_number = int(input("Enter product id: "))
    updated_id = int(input("Enter updating id number: "))
    update_name = input('Enter new product name: ')
    update_price = format("Enter new product price: ")

    if id_number in product_details[id_number]:
        product_details[id_number] = updated_id
        product_details[id_number]["name"] =  update_name
        product_details[id_number]["price"] =  update_price

        print("Product details updated")

    else:
        print("Please enter the valid id number")



def view_data():
    for k, v in product_details.items():
        print(f"{k} : {v}")


while True:
    print("""
Wellcome to TO-DO App
          
--------------------------------
          
Please choose one of the below

1. Add data
2. Delete data
3. Update data
4. View data
5. Not any or exit

""")
    
    user_choice = int(input("Enter your choice: "))
    if user_choice == 1:
        add_data()
    
    elif user_choice == 2:
        delete_data()

    elif user_choice == 3:
        update_data()

    elif user_choice == 4:
        view_data()

    elif user_choice == 5:
        print("Thank you for visiting my app")
        break

    else:
        print("Please enter valid choise")
        break
