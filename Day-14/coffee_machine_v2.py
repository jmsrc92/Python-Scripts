MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Program start

machine_on = True
machine_money = 0

def print_report():
    global machine_money
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f"Water: {water}")
    print(f"Milk: {milk}")
    print(f"Coffee: {coffee}")
    print(f"Money: ${machine_money}")
    return

def check_resources(chosen_drink):
    """Loops through coffee ingredients returns false if not enough resources
    returns True if levels are enough to make a drink"""
    for item in MENU[chosen_drink]["ingredients"]: # Every ingredient within chosen drink
        if MENU[chosen_drink]["ingredients"][item] >= resources[item]:
            print(f"There is not enough {item} .")
            return False
        else: return True


def process_coins(total_quarters=0, total_dimes=0, total_nickles=0, total_pennies=0):
    """Returns sum of given amount of change"""
    total_quarters *= 0.25
    total_dimes *= 0.10
    total_nickles *= 0.05
    total_pennies *= 0.01
    return total_quarters + total_dimes + total_nickles + total_pennies 


def make_coffee(chosen_drink):
    """Deducts coffee values from machine"""
    for item in MENU[chosen_drink]["ingredients"]:
        resources[item] -= MENU[chosen_drink]["ingredients"][item]
        return


while machine_on:

    choice = input("What would you like (espresso/latte/cappuccino): ")

    if choice.lower() == "off":
        machine_on = False
    elif choice.lower() == "report":
        print_report()
        machine_on = False
    elif choice not in MENU:
        print("Invalid choice")
    else:
        check_resources(choice)
    
    if check_resources(choice) == False:
        machine_on = False

    num_quarters = int(input("How many quarters? "))
    num_dimes = int(input("How many dimes? "))
    num_nickles = int(input("How many nickles? "))
    num_pennies = int(input("How many pennies? "))

    change = process_coins(num_quarters, num_dimes, num_nickles, num_pennies)

    if change >= MENU[choice]["cost"]: # Adds change to machine if enough money for drink
        machine_money += change
        leftover_change = change - MENU[choice]["cost"]
        print(f"Here is ${leftover_change} in change. ") # Print Total change given
        make_coffee(choice)
    else:
        print("Sorry that's not enough money. Money refunded")    
