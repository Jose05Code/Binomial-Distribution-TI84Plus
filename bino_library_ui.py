def menu() -> None:
    print("===============================")
    print("Welcome to the Bino Library")
    print("1. P(x > a)")
    print("2. P(x >= a)")
    print("3. P(x < a)")
    print("4. P(x <= a)")
    print("5. P(x = a)")
    print("===============================")
    choice = get_user_choice(5)

def get_user_choice(number_of_choices: int) -> int:
    while True:
        choice = input(f"Enter your choice (1-{number_of_choices}): ")
        if choice <= 0 or choice > number_of_choices:
            print(f"Invalid choice. Please enter a number between 1 and {number_of_choices}.")
        else:
            return choice

def probability_greater_than(choice: int) -> None:
    print("Calculating P(x > a)...")
    # Placeholder for actual calculation logic
    pass

def probability_greater_equal(choice: int) -> None:
    print("Calculating P(x >= a)...")
    # Placeholder for actual calculation logic
    pass

def probability_less_than(choice: int) -> None:
    print("Calculating P(x < a)...")
    # Placeholder for actual calculation logic
    pass

def probability_less_equal(choice: int) -> None:
    print("Calculating P(x <= a)...")
    # Placeholder for actual calculation logic
    pass

def probability_equal(choice: int) -> None:
    print("Calculating P(x = a)...")
    # Placeholder for actual calculation logic
    pass