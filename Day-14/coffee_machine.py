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

drink = input("What would you like (espresso/latte/cappuccino): ")

print("Please insert coins.")

no_quarters = input("How many quarters?")
no_dimes = input("How many dimes?")
no_nickles = input("How many nickles?")
no_pennies = input("How many pennies?")

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

#  while coffee_machine == "on":

if drink == "off":
    coffee_machine = "off"
elif drink == "report":
    print_report()




