


# 1.Prompt user by asking “​What would you like? (espresso/latte/cappuccino):​
# ”a.Check the user’s input to decide what to do next.
# b.The prompt should show every time action has completed,
#  e.g. once the drink is dispensed. The prompt should show again to serve the next customer.

coffee_types = ["espresso", "latte", "cappuccino"]

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 200,
    "milk": 500,
    "coffee": 100
}

profit = 0

def print_report():
    """Prints available resources out"""

    print("Available Resources")
    for key in resources:
        print(f"{key.capitalize()}: {resources[key]}")
    print(f"Profit: {profit}")


def check_resources(choice):
    """Checks if we have enough resources to complete order"""

    resources_available = "available"
    for key in MENU[choice]["ingredients"]:
        # print(resources[key], MENU[choice]["ingredients"][key])
        if resources[key] < MENU[choice]["ingredients"][key]:
            resources_available = key


        return resources_available


def process_coins():

    total = 0
    total += float(input("How many quarters?: ")) * 0.25
    total += float(input("How many dimes?: ")) * 0.10
    total += float(input("How many nickles?: ")) * 0.5
    total += float(input("How many pennies?: ")) * 0.01

    return total
    # quarters = float(input("How many quarters?: ")) * 0.25
    # dimes = float(input("How many dimes?: ")) * 0.10
    # nickles = float(input("How many nickles?: ")) * 0.5
    # pennies = float(input("How many pennies?: ")) * 0.01


def check_money_is_enough(amount_paid, choice):
    if amount_paid >= MENU[choice]["cost"]:
        return True
    else:
        return False


def calculate_change(amount_paid, choice):

    return amount_paid - MENU[choice]["cost"]


# Turn off
stop_machine = False


while not stop_machine:

    user_choice = str(input("What would you like? (espresso/latte/cappuccino): ").lower())

    if user_choice in MENU:
        # Valid choice
        print(f"{user_choice} cost: {MENU[user_choice]['cost']}")
        order_status = check_resources(user_choice)
        if order_status == "available":
            paid_coins = process_coins()
            if check_money_is_enough(paid_coins, user_choice):
                return_change = calculate_change(paid_coins, user_choice)
                profit += paid_coins - return_change
                print(f"Here is your change: {return_change}")
                print(f"enjoy your {user_choice}")
            else:
                print(f"Insufficient funds, please enter more coins to complete order")
        else:
            print(f"Not enough {order_status} to complete order sorry ")
    elif user_choice == "report":
        # Report
        print_report()
    elif user_choice == "off":
        # Turn off
        stop_machine = True
    else:
        # Invalid choice
        print("Incorrect choice, please try again")


# 2.Turn off the Coffee Machine by entering “​off​” to the prompt.a.For maintainers of the coffee machine, they can use “off”
# as the secret word to turn off the machine. Your code should end execution when this happens

# 3.Print report.a.When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5

# 4.Check resources sufficient?a.When the user chooses a drink, the program should check if there are enough
# resources to make that drink.b.E.g. if Latte requires 200ml water but there is only 100ml left in the machine.
#  It should not continue to make the drink but print: “​Sorry there is not enough water.​”c.The same should happen if another resource is depleted,
#   e.g. milk or coffee

# 5.Process coins.a.If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.b.Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01c.
# Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52