from data import MENU, resources

flag = True


def enter_command():
    command = input("What would you like? (espresso/latte/cappuccino): ")
    if command == 'off':
        return
    if command == 'report':
        report()
        command = enter_command()
    return command


def check_resources(chosen_drink):
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    drink_water = MENU[chosen_drink]['ingredients']['water']
    drink_coffee = MENU[chosen_drink]['ingredients']['coffee']
    if 'milk' in MENU[chosen_drink]['ingredients']:
        drink_milk = MENU[chosen_drink]['ingredients']['milk']
        if milk < drink_milk:
            return print("Sorry there is not enough milk.")
    if water < drink_water:
        return print("Sorry there is not enough water.")
    if coffee < drink_coffee:
        return print("Sorry there is not enough coffee.")
    return True


def make_drink(chosen_drink):
    keys = MENU[chosen_drink]["ingredients"].keys()
    for key in keys:
        resources[key] -= MENU[chosen_drink]["ingredients"][key]


def report():
    for item in resources:
        if item == 'water' or item == 'milk':
            units_of_measurement = 'ml'
            print(f"{item.capitalize()}: {resources[item]}{units_of_measurement}")
        if item == 'coffee':
            units_of_measurement = 'g'
            print(f"{item.capitalize()}: {resources[item]}{units_of_measurement}")
        if item == 'money':
            print(f"{item.capitalize()}: ${resources[item]}")


def payment(chosen_drink):
    penny = 0.01
    nickel = 0.05
    dime = 0.10
    quarter = 0.25

    print("Please insert coins.")

    quarters = float(input(" how many quarters?: "))
    dimes = float(input(" how many dimes?: "))
    nickles = float(input(" how many nickles?: "))
    pennies = float(input(" how many pennies?: "))
    coins_sum = quarter * quarters + nickel * nickles + dime * dimes + penny * pennies

    price = MENU[chosen_drink]["cost"]

    if coins_sum >= price:
        if coins_sum > price:
            change = round(coins_sum - price, 2)
            print(f"Here is ${change} dollars in change.")
        if resources.get('money') is None:
            resources.update({"money": price})
        else:
            update_money = resources.get('money') + price
            resources.update({"money": update_money})
        return True
    else:
        return print("Sorry that's not enough money. Money refunded.")


while flag:
    chosen_drink = enter_command()
    if chosen_drink is None:
        flag = False
        break
    if check_resources(chosen_drink) is True:
        payment_drink = payment(chosen_drink)
        if payment_drink is True:
            make_drink(chosen_drink)
            print(f"Here are your {chosen_drink}. Thank you for coming! Enjoy!!")
