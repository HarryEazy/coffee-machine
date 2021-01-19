



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


