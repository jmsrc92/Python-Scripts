from coffee_menu import MENU
from coffee_menu import resources


coffee_machine_on = True
coffee_machine_cash = 0

while coffee_machine_on:




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


    def print_report():
        water = resources["water"]
        milk = resources["milk"]
        coffee = resources["coffee"]
        print(f"Water: {water}")
        print(f"Milk: {milk}")
        print(f"Coffee: {coffee}")
        print(f"Money: ${coffee_machine_cash}")


    drink = input("What would you like (espresso/latte/cappuccino): ")

    if drink == "off":
        coffee_machine_on = False
    elif drink == "report":
        print_report()
        drink = input("What would you like (espresso/latte/cappuccino): ")

    print("Please insert coins.")

    num_quarters = int(input("How many quarters? "))
    num_dimes = int(input("How many dimes? "))
    num_nickles = int(input("How many nickles? "))
    num_pennies = int(input("How many pennies? "))

    total_user_money = cash_total(num_quarters, num_dimes, num_nickles, num_pennies)


    def check_resources(chosen_drink):
        """Checks coffee ingredient values against machine level values returns nothing"""
        global coffee_machine_on
        coffee_ingredients = MENU[chosen_drink]["ingredients"]
        for item in coffee_ingredients:
            coffee_ingredient_value = MENU[chosen_drink]["ingredients"][item]
            resource_ingredient_value = resources[item]
            if resource_ingredient_value < coffee_ingredient_value:
                print(f"Sorry there is not enough {item}")
                coffee_machine_on = False
            else:
                resources[item] = resource_ingredient_value - coffee_ingredient_value #update dictionary value


    def check_transaction(user_money, chosen_drink, coffee_cash_total):
        drink_cost = MENU[chosen_drink]["cost"]
        if user_money < drink_cost:
            print("Sorry that's not enough money. Money refunded.")
        else:
            change = round(user_money - drink_cost, 2)
            coffee_cash_total += drink_cost
            print(f"Here is ${change} dollars in change.")
        return coffee_cash_total

    check_resources(drink)
    coffee_machine_cash = check_transaction(total_user_money, drink, coffee_machine_cash)