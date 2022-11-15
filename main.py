from details import *

ingredients_left = {"water":3000 ,"milk":1000, "coffee": 100 }


print("welcome to stg coffe machine ")
print("what would u like to have")
print("we have esspresso, latte, capucchhino ")

def check():
    if inserted > menu['espresso']['cost']:
        print(f"here is ur {inserted - menu['espresso']['cost']} change")
    elif inserted < menu['espresso']['cost']:
        print(f" not enough money inserted")


def money():
    tens = int(input("enter the number tens inserted"))
    twenties = int(input("enter the number of twenties inserted"))
    fiftys = int(input("enter the number of fifties inserted"))
    hundreds = int(input("enter the number of hundreds inserted"))
    total = tens*10 + twenties*20 + fiftys*50 + hundreds*100
    return total


while(True):
    drink = input("wat do u preffer, press 1 for esspresso 2 for latte and 3 for capucchhino and report for report")

    if drink == "1":
        print(f"the cost of esspresso is {menu['espresso']['cost']}")
        inserted = money()
        check()
        ingredients_left["water"] -=  50
        ingredients_left["coffee"] -=  18

    elif drink == "2":
        print(f"the cost of esspresso is {menu['latte']['cost']}")
        inserted = money()
        check()
        ingredients_left["water"] -=  200
        ingredients_left["coffee"] -=  24
        ingredients_left["milk"] -= 150
    elif drink == "3":
        print(f"the cost of esspresso is {menu['cappuccino']['cost']}")
        inserted = money()
        check()
        ingredients_left["water"] -=  200
        ingredients_left["coffee"] -=  24
        ingredients_left["milk"] -= 100
    elif drink == "report":
        print(ingredients_left)
