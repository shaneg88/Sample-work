# import tabulate function 
from tabulate import tabulate

#========The beginning of the class==========
class Shoe:

    # initialise the class attributes
    def __init__(self, country, code, product, cost, quantity):
        
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # set up functions for within class    
    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"{self.country} {self.code} {self.product} {self.cost} {self.quantity}"


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============
# open text file and add shoes to list using try/except incase file does not exist
def read_shoes_data():

    try:
        # clear shoe list first so as not appending to the list each time this function is run
        shoe_list.clear()
        with open("inventory.txt", "r", encoding = "utf-8") as f:
            next(f) # used to skip first line
            for line in f:
                info = line.replace("\n", "").split(",")
                shoes = Shoe(info[0], info[1], info[2], int(info[3]), int(info[4]))
                shoe_list.append(shoes)
        
        print("Inventory list created")

    except FileNotFoundError:
        print("The file can not be found, please check the file is in the correct folder")
        pass

def capture_shoes():
    # ask which country shoes are in
    shoe_country = input("Which country are the shoes from:")

    # use while loop to add shoe code, as all start with SKU ask only for ints
    while True:
        try:
            code = int(input("Enter the product code (numbers only):"))
        
        except ValueError:
            print("Only enter the numbers associated with the code")
            continue

        else:
            shoe_code = "SKU" + str(code)
            break

    # ask for shoe name        
    shoe_product = input("What is the name of the shoe:")

    # ask for shoe cost using try/except to make sure numbers are entered
    # using ints as all other costs are whole numbers in text file
    while True:
        try:
            shoe_cost = int(input("Enter the cost of the shoes (numbers only):"))

        except ValueError:
            print("Only enter the numbers associated with cost")
            continue

        else:
            break

    # ask for quantity using try/except so only numbers are added
    while True:
        try:
            shoe_quantity = int(input("Enter the stock quantity (numbers only):"))

        except ValueError:
            print("Only enter quantity in numbers")
            continue

        else:
            break

    # create new shoe object with inputted info
    new_shoe = Shoe(shoe_country, shoe_code, shoe_product, shoe_cost, shoe_quantity)

    # add new shoe to inventory text file
    with open("inventory.txt", "a", encoding = "utf-8") as f:
        new_shoe_line = (f"\n{new_shoe.country},{new_shoe.code},{new_shoe.product},{new_shoe.cost},{new_shoe.quantity}")
        f.write(new_shoe_line)
        # add shoe to shoe list
        shoe_list.append(new_shoe)
        print("New shoe successfully added")

def view_all():
    # use tabulate to print out info on all shoes
    country = []
    code = []
    product = []
    cost = []
    quantity = []
    for item in range(len(shoe_list)):
        country.append(shoe_list[item].country)
        code.append(shoe_list[item].code)
        product.append(shoe_list[item].product)
        cost.append(shoe_list[item].cost)
        quantity.append(shoe_list[item].quantity)

    # create dictionary to make table formatting easier
    table = {
        "Country": country,
        "Code": code,
        "Product": product,
        "Cost": cost,
        "Quantity": quantity,
    }
    print(tabulate(table, headers = ["Country", "Code", "Product", "Cost", "Quantity"]))

def re_stock():
    # search through shoes list and find the lowest quantity
    lowest = min(shoe_list, key = lambda shoes: shoes.quantity)
    print(f"The shoe with the lowest stock is {lowest.product}, there is only {lowest.quantity} left")

    # ask if stock should be increased
    up_stock = input("Do you wish to restock this item (y/n): ").lower()
    if up_stock == "y":
        while True:
            try:
                num = int(input("How much should stock be increased by:"))

            except ValueError:
                print("Stock increase should be numbers only")
                continue

            else:
                break

        new_stock = int(lowest.quantity) + num
        lowest.quantity = new_stock

        with open("inventory.txt", "w", encoding = "utf-8") as f:
            f.write("Country,Code,Product,Cost,Quantity")
            for shoe in shoe_list:
                f.writelines(f"\n{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}")
            
        # clear shoe_list and repopulate with new data
        shoe_list.clear()
        with open("inventory.txt", "r", encoding = "utf-8") as f:      
            next(f) # used to skip first line
            for line in f:
                info = line.replace("\n", "").split(",")
                shoes = Shoe(info[0], info[1], info[2], int(info[3]), int(info[4]))
                shoe_list.append(shoes)


        print("Stock updated")

    else:
        print("Returned to menu")            

def search_shoe():
    # search using the SKU number and print details
    # create exists variable to add so non matching codes can be ignored
    exists = False
    # ask for SKU number
    while True:
        try:
            to_search = int(input("Enter the SKU code (numbers only):"))

        except ValueError:
            print("Input numbers only")
            continue

        else:
            break

    search = "SKU" + str(to_search)

    country = []
    code = []
    product = []
    cost = []
    quantity = []
    for item in range(len(shoe_list)):
        if search == shoe_list[item].code:
            country.append(shoe_list[item].country)
            code.append(shoe_list[item].code)
            product.append(shoe_list[item].product)
            cost.append(shoe_list[item].cost)
            quantity.append(shoe_list[item].quantity)
            exists = True
        else:
            continue

        table = {
            "Country": country,
            "Code": code,
            "Product": product,
            "Cost": cost,
            "Quantity": quantity,
        }

    # print table but only if searched code exists
    if exists:
        print(tabulate(table, headers = ["Country", "Code", "Product", "Cost", "Quantity"]))
        
    # if searched code not found
    else:
        print("Searched code not found")      
    

def value_per_item():
    # uses table method from earlier functions but adds a value field to display value of stock
    country = []
    code = []
    product = []
    cost = []
    quantity = []
    value = []
    for item in range(len(shoe_list)):
        country.append(shoe_list[item].country)
        code.append(shoe_list[item].code)
        product.append(shoe_list[item].product)
        cost.append(shoe_list[item].cost)
        quantity.append(shoe_list[item].quantity)
        total_value = int(shoe_list[item].cost) * int(shoe_list[item].quantity)
        value.append(total_value)

    # create dictionary to make table formatting easier
    table = {
        "Country": country,
        "Code": code,
        "Product": product,
        "Cost": cost,
        "Quantity": quantity,
        "Value": value
    }
    print(tabulate(table, headers = ["Country", "Code", "Product", "Cost", "Quantity", "Value"]))
    

def highest_qty():
    # search through list and find highest quantity
    # reverse of lowest method used earlier
    highest = max(shoe_list, key = lambda shoes: shoes.quantity)
    # think this is what it means by advertise it on sale
    print(f"The most popular shoe is {highest.product}, buy now before you miss out!")
    
#==========Main Menu=============

# create main menu so each function can be used as needed
main_menu = """
c - create inventory list
a - add new shoe to inventory
va - view all stock
rs - restock the lowest quantity item
s - search shoe to see details 
tv - print total value of each item in shoe stock
h - show item to put on sale
e - exit programme
"""

# create while loop
while True:
    choice = input(main_menu).strip().lower()

    if choice == "c":
        read_shoes_data()

    elif choice == "a":
        capture_shoes()

    elif choice == "va":
        view_all()

    elif choice == "rs":
        re_stock()

    elif choice == "s":
        search_shoe()

    elif choice == "tv":
        value_per_item()

    elif choice == "h":
        highest_qty()

    elif choice == "e":
        print("Goodbye")
        exit()

    else:
        print("Incorrect option, please retry")