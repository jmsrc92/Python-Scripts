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
coffee_machine_cash = 0
#  while coffee_machine == "on":

drink = input("What would you like (espresso/latte/cappuccino): ")


def cash_total(total_quarters=0, total_dimes=0, total_nickles=0, total_pennies=0):
    quarter_val = 0.25
    dime_val = 0.10
    nickle_val = 0.05
    penny_val = 0.01
    total_quarters *= quarter_val
    total_dimes *= dime_val
    total_nickles *= nickle_val
    total_pennies *= penny_val
    return total_quarters + total_dimes + total_nickles + total_pennies


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

num_quarters = int(input("How many quarters? "))
num_dimes = int(input("How many dimes? "))
num_nickles = int(input("How many nickles? "))
num_pennies = int(input("How many pennies? "))

total_user_money = cash_total()


def check_resources(chosen_drink):
    """Checks coffee ingredient values against machine level values returns nothing"""
    coffee_ingredients = MENU[chosen_drink]["ingredients"]
    for item in coffee_ingredients:
        coffee_ingredient_value = MENU[chosen_drink]["ingredients"][item]
        resource_ingredient_value = resources[item]
        if resource_ingredient_value < coffee_ingredient_value:
            print(f"Sorry there is not enough {item}")
        resource_ingredient_value -= coffee_ingredient_value


def check_transaction(user_money, chosen_drink, coffee_cash_total):
    if user_money < chosen_drink:
        print("Sorry that's not enough money. Money refunded.")
    else:
        coffee_cash_total -= user_money
        print(f"Here is {coffee_cash_total} dollars in change.”")
    return coffee_cash_total
