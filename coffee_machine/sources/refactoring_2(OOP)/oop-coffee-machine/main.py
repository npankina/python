from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO-1: Print report
# TODO-2: Check resources sufficient
# TODO-3: Process coins
# TODO-4: Check transaction successful
# TODO-5: Make coffee
#
menu = Menu()
make_drink = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    choice = input(f"What would you like? ({menu.get_items()}): ").lower()
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        make_drink.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if make_drink.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            make_drink.make_coffee(drink)
