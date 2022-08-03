from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == 'off':
        is_on = False

    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()

    else:
        drink = menu.find_drink(choice)
        can_make = coffee_maker.is_resource_sufficient(drink)
        if can_make:
            payment_done = money_machine.make_payment(drink.cost)
            if payment_done:
                coffee_maker.make_coffee(drink)

