import LIB_BIN as ui

def main():
    switcher = {
        1: ui.probability_greater_than,
        2: ui.probability_greater_equal,
        3: ui.probability_less_than,
        4: ui.probability_less_equal,
        5: ui.probability_equal,
    }
    max_option = max(k for k in switcher.keys() if k != 0)
    while True:
        ui.menu()
        choice = ui.get_user_choice(max_option)
        func = switcher.get(choice)
        func()

main()