def menu():
    print("===============================")
    print("Welcome to the Bino Library")
    print("1. P(x > a)")
    print("2. P(x >= a)")
    print("3. P(x < a)")
    print("4. P(x <= a)")
    print("5. P(x = a)")
    print("===============================")
    choice = get_user_choice(5)

def get_user_choice(number_of_choices):
    while True:
        choice = input(f"Enter your choice (1-{number_of_choices}): ")
        if choice <= 0 or choice > number_of_choices:
            print(f"Invalid choice. Please enter a number between 1 and {number_of_choices}.")
        else:
            return choice

