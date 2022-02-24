from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
tassimo = CoffeeMaker()
money = MoneyMachine()
tassimo_on = True

while tassimo_on == True:
    user_choice = input(f"What would you like? {menu.get_items()} : ") #Takes input from list of drinks

    if user_choice == "report":
        tassimo.report()
        print(f"Money ${money.profit}")
    elif user_choice == "off":
        tassimo_on = False
    else:
        drink = menu.find_drink(user_choice) #finds the drink entered by user and returns object
        if tassimo.is_resource_sufficient(drink) == None:
            print("Not enough resources") # needs testing
        else:    
            money.make_payment(drink.cost)
            tassimo.make_coffee(drink)
      
