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

profit = 0

quarter_value = 0.25
dime_value = 0.1
nickle_value = 0.05
penny_value = 0.01


def main_function():
    is_over = False
    while not is_over:

        def check_resources():
            if coffee_type == "espresso":
                coffee_list["ingredients"]["milk"] = 0
            for i in resources:
                # ingredient = coffee_list["ingredients"]
                if resources[i] < coffee_list["ingredients"][i]:
                    print(f"Sorry there is not enough {i}.")
                    main_function()

        def process_coins():
            quarters = int(input("how many quarters?"))
            dimes = int(input("how many dime?"))
            nickles = int(input("how many nickles?"))
            pennies = int(input("how many pennies?"))
            total = (quarters * quarter_value) + (dimes * dime_value) + (nickles * nickle_value) + (
                        pennies * penny_value)
            return total

        def check_transaction(total):
            global profit
            if total < coffee_list["cost"]:
                print("sorry that\'s not enough. Money refunded.")
            else:
                change = float(total - 2.5)
                print(f"Here is $ {round(change, 2)} in change.")
                profit = profit + coffee_list["cost"]

        def make_coffee(coffee_type):
            resources["water"] = resources["water"] - coffee_list["ingredients"]["water"]
            resources["milk"] = resources["milk"] - coffee_list["ingredients"]["milk"]
            resources["coffee"] = resources["coffee"] - coffee_list["ingredients"]["coffee"]
            print(f"Here is your {coffee_type} ☕️. Enjoy!")

        coffee_type = input("What would you like? (espresso/latte/cappuccino): ")

        if coffee_type == "report":
            print(
                f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${profit}')
        elif coffee_type == "espresso" or coffee_type == "latte" or coffee_type == "cappuccino":
            coffee_list = MENU[coffee_type]
            print("Please insert coins.")
            check_resources()
            payment = process_coins()
            check_transaction(payment)
            make_coffee(coffee_type)
        elif coffee_type == "off":
            exit()


main_function()
