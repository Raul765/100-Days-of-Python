menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":0,
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

coins={
    "quarters":0.25,
    "dimes":0.10,
    "nickels":0.05,
    "pennies":0.01
}

money=0

def machine():

    global resources
    global money
    is_order=True
    money_temp=0

    order=input("What would you like? (espresso/latte/cappuccino):​ ").lower()

    if order=="report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: ${money}")
        is_order=False

    elif order=="off":
        return

    if is_order:
        for i in resources:
            if resources[i]< menu[order]["ingredients"][i]:
                print(f"Sorry, not enough {i}")
                is_order=False
                break
    
    if is_order:
        print("Please insert coins")
        for i in coins:
            money_temp+=int(input(f"How many {i}?: "))*coins[i]

        if money_temp>=menu[order]["cost"]:
            change=money_temp-menu[order]["cost"]
            change=round(change,2)
            
            if change>0:
                print(f"Here is ${change} in change.")
        else:
            print("Sorry, not enough money. Money refunded")
            is_order=False

    if is_order:
        for i in resources:
            resources[i]-=menu[order]["ingredients"][i]
        money+=menu[order]["cost"]
        print(f"Here is your {order} ☕ enjoy!")

    machine()

machine()


    

