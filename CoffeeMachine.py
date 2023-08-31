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
is_finish = True
payment = 0


def check_resources(ordered_drink, resources_mount):
    for item in ordered_drink:
        if ordered_drink[item] > resources_mount[item]:
            print('Sorry there is not enough water.')
            return False
        else:
            return True


def process_coins():
    total = int(input("How many quarters do you pay?")) * 0.25
    total += int(input("How many dimes do you pay?")) * 0.1
    total += int(input("How many nickles do you pay?")) * 0.05
    total += int(input("How many pennies do you pay?")) * 0.01
    return total


def check_transaction(payment_mount, cost):
    global profit
    change = payment_mount - cost
    if payment_mount < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        print(f"Here is ${change} dollars in change.")
        profit += payment - change
        return True


def make_coffee(drink, resource, order):
    for item in drink:
        resource[item] -= drink[item]
    print(f"Here is your {order}. Enjoy!")


while is_finish:
    client_wish = input("What would you like? (espresso/latte/cappuccino):")
    if client_wish == "off":
        is_finish = False
    elif client_wish == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[client_wish]
        if check_resources(drink['ingredients'], resources):
            payment = process_coins()
            if check_transaction(payment, drink['cost']):
                make_coffee(drink['ingredients'], resources, client_wish)
