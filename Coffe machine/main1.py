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
    "water": 900,
    "milk": 700,
    "coffee": 100,
}
from art import logo
c = 0
money11 = 0
money2 = water = waterr = milk = milkr = coffee = coffer = 0


def resources1():
    global water, milk, coffee, waterr, milkr, coffer
    for i in resources:
        if i == "water":
            waterr = resources[i]
        elif i == "milk":
            milkr = resources[i]
        elif i == "coffee":
            coffer = resources[i]
    if waterr < water:
        return "Oops!Not enough water."
    elif milkr < milk:
        return "Not enough Milk,Sorry!"
    elif coffer < coffee:
        return "Sorry!Not enough coffee."
    return f"The machine has all the ingredients of {desire}.You need to enter ${c} to buy it."


def money1(money):
    global c, money2
    if money >= c:
        money1 = money - c
        money1 = round(money1, 2)
        money2 += c
        resources["money"] = money2
        enough_money()
        return f"You gave total ${money}.Here is your exchange ${money1}.\nHere is your drink.Enjoy!"
    elif money < c:
        return f"Insufficient funds.Total funds required are ${c} while you have ${money}.Add more money.Thanks!"


def enough_money():
    global waterr, water, milk, milkr, coffee, coffer
    for i in resources:
        if i == 'water':
            resources["water"] = waterr - water
        elif i == "milk":
            resources["milk"] = milkr - milk
        elif i == "coffee":
            resources["coffee"] = coffer - coffee


def espresso():
    global c
    global water, coffee, milk
    milk = 0
    for i in MENU:
        if i == "espresso":
            a = MENU[i]
            for i in a:
                if i == "ingredients":
                    b = a[i]
                    for i in b:
                        if i == "water":
                            water = b[i]
                        elif i == "coffee":
                            coffee = b[i]
                if i == 'cost':
                    c = a[i]
    return resources1()


def latte():
    global c, water, milk, coffee
    for i in MENU:
        if i == "latte":
            a = MENU[i]
            for i in a:
                if i == "ingredients":
                    b = a[i]
                    for i in b:
                        if i == "water":
                            water = b[i]
                        elif i == "milk":
                            milk = b[i]
                        elif i == "coffee":
                            coffee = b[i]
                if i == 'cost':
                    c = a[i]
    return resources1()


def cappuccino():
    global c, water, milk, coffee
    for i in MENU:
        if i == "cappuccino":
            a = MENU[i]
            for i in a:
                if i == "ingredients":
                    b = a[i]
                    for i in b:
                        if i == "water":
                            water = b[i]
                        elif i == "milk":
                            milk = b[i]
                        elif i == "coffee":
                            coffee = b[i]
                if i == 'cost':
                    c = a[i]

    return resources1()


def report1():
    global water, milk, coffee, waterr, milkr, coffer
    global money11
    for i in resources:
        if i == "water":
            waterr = resources[i]
        elif i == "milk":
            milkr = resources[i]
        elif i == "coffee":
            coffer = resources[i]
        elif i == "money":
            money11 = resources[i]
    pri  t(f"Water: {waterr}\nMilk: {milkr}\nCoffee: {coffer}\nMoney: ${money11}")

turn_of   = False
print(l  go)
while n  t turn_off:
    des  re = input("What would you like? (espresso/latte/cappuccino): ")
    if   esire == 'latte':
        choice = latte()
        print(choice)
        if choice == "Oops!Not enough water." or choice == "Not enough Milk,Sorry!" or choice == "Sorry!Not enough coffee.":
            ask_money = False
        else:
            ask_money = True
    elif desire == "report":
        report1()
        ask_money = False
    elif desire == "cappuccino":
        choice = cappuccino()
        print(choice)
        if choice == "Oops!Not enough water." or choice == "Not enough Milk,Sorry!" or choice == "Sorry!Not enough coffee.":
            ask_money = False
        else:
            ask_money = True
    elif desire == "espresso":
        choice = espresso()
        print(choice)
        if choice == "Oops!Not enough water." or choice == "Not enough Milk,Sorry!" or choice == "Sorry!Not enough coffee.":
            ask_money = False
        else:
            ask_money = True
    elif desire == "off":
        ask_money = False
        turn_off = True
    else:
        print("Invalid input.check spells.")
        turn_off = False
        ask_money = False
    while ask_money:
        quater = float(input("How many Quaters you want to enter: "))
        dime = float(input("How many Dimes you want to enter: "))
        nickel = float(input("HOw many nickles you want to enter: "))
        penny = float(input("How many pennies you want to enter: "))
        money = quater * 0.25 + dime * 0.10 + nickel * 0.05 + penny * 0.01
        money = round(money, 2)
        print(money1(money))
        ask_money = False
