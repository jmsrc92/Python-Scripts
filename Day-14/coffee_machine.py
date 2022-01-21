from coffee_menu import MENU
from coffee_menu import resources

# """
# what would you like {latte}
# please insert coins
# how many quarters?
# how many dimes
# how many nickels?
# how many pennies?
# here is ($X) in change
# here is your {latte} enjoy{coffee emoji}!
# adjust report
# """
coffee_machine = "on"

#  while coffee_machine == "on":

drink = input("What would you like (espresso/latte/cappuccino): ")


def cash_total():
    quarter_val = 0.25
    dime_val = 0.10
    nickle_val = 0.05
    penny_val = 0.01


def print_report(money=0):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f"Water: {water}")
    print(f"Milk: {milk}")
    print(f"Coffee: {coffee}")
    print(f"Money: ${money}")


if drink == "off":
    coffee_machine = "off"
elif drink == "report":
    print_report()

print("Please insert coins.")

# no_quarters = input("How many quarters? ")
# no_dimes = input("How many dimes? ")
# no_nickles = input("How many nickles? ")
# no_pennies = input("How many pennies? ")

def check_resources(chosen_drink):
    """Checks coffee ingredient values against machine level values returns nothing"""
    coffee_ingredients = MENU[chosen_drink]["ingredients"]
    for item in coffee_ingredients:
        coffee_ingredient_value = MENU[chosen_drink]["ingredients"][item]
        resource_ingredient_value = resources[item]
        if resource_ingredient_value < coffee_ingredient_value:
            print(f"Sorry there is not enough {item}")
        resource_ingredient_value -= coffee_ingredient_value


check_resources(drink)