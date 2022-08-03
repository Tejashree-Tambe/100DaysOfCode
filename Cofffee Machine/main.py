from menu_resources import MENU, resources
money = 0


def add_money(coffee_cost):
    global money
    money += coffee_cost


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def get_coffee_cost(coffee_flavour):
    cost_of_coffee = 0

    if coffee_flavour == 'espresso':
        cost_of_coffee = MENU['espresso']['cost']

    elif coffee_flavour == 'latte':
        cost_of_coffee = MENU['latte']['cost']

    elif coffee_flavour == 'cappuccino':
        cost_of_coffee = MENU['cappuccino']['cost']

    return cost_of_coffee


def get_coins():
    print("Please insert coins.")
    quarters_given = int(input("How many quarters?: "))
    dimes_given = int(input("How many dimes?: "))
    nickels_given = int(input("How many nickels?: "))
    pennies_given = int(input("How many pennies?: "))

    total_money = (0.25 * quarters_given) + (0.10 * dimes_given) + (0.05 * nickels_given) + (0.01 * pennies_given)

    return total_money


def resources_needed(type_of_coffee):
    water_needed = MENU[type_of_coffee]['ingredients']['water']
    milk_needed = MENU[type_of_coffee]['ingredients']['milk']
    coffee_needed = MENU[type_of_coffee]['ingredients']['coffee']
    resources_in_need = [water_needed, milk_needed, coffee_needed]

    return resources_in_need


def make_coffee(type_of_coffee):
    resources_in_need = resources_needed(type_of_coffee)
    resources['water'] -= resources_in_need[0]
    resources['milk'] -= resources_in_need[1]
    resources['coffee'] -= resources_in_need[2]


def check_resources(type_of_coffee):
    resources_in_need = resources_needed(type_of_coffee)

    water_remaining = resources['water']
    milk_remaining = resources['milk']
    coffee_remaining = resources['coffee']

    if water_remaining < resources_in_need[0]:
        print("Sorry there is not enough water")
        return False

    elif milk_remaining < resources_in_need[1]:
        print("Sorry there is not enough milk")
        return False

    elif coffee_remaining < resources_in_need[2]:
        print("Sorry there is not enough coffee")
        return False

    else:
        make_coffee(type_of_coffee)
        return True
        # print(type_of_coffee)


resources_exists = True


def start_machine():
    global resources_exists
    while resources_exists:
        coffee_type = input("What would you like? (espresso/latte/cappuccino): ")

        if coffee_type == 'espresso' or coffee_type == 'latte' or coffee_type == 'cappuccino':
            resources_remaining = check_resources(coffee_type)
            if resources_remaining:
                coffee_cost = get_coffee_cost(coffee_type)
                total_money_given = get_coins()
                change = total_money_given - coffee_cost
                print(f"Here is ${change:.2f} in change")
                add_money(coffee_cost)

        elif coffee_type == 'off':
            resources_exists = False

        else:
            print_report()


start_machine()
