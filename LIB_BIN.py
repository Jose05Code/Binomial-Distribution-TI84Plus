def menu() -> None:
    print("===============================")
    print("Welcome to the Bino Library")
    print("1. P(x > a)")
    print("2. P(x >= a)")
    print("3. P(x < a)")
    print("4. P(x <= a)")
    print("5. P(x = a)")
    print("0. Exit")
    print("===============================")

def get_user_choice(number_of_choices: int) -> int:
    while True:
        choice = int(input(f"Enter your choice (0-{number_of_choices}): "))
        if choice < 0 or choice > number_of_choices:
            print(f"Invalid choice. Please enter a number between 0 and {number_of_choices}.")
        else:
            return choice
        
def get_parameters() -> tuple[int, float, int]:
    while True:
        try:
            n = int(input("Enter the number of trials (n >= 0): "))
            if n < 0:
                print("Number of trials must be a non-negative integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a non-negative integer for n.")
    while True:
        try:
            p = float(input("Enter the probability of success in decimal (0 <= p <= 1): "))
            if p < 0 or p > 1:
                print("Probability must be between 0 and 1 (inclusive).")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a decimal number between 0 and 1 for p.")
    while True:
        try:
            a = int(input("Enter the value of a (a >= 0): "))
            if a < 0:
                print("Value of a must be a non-negative integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a non-negative integer for a.")
    return n, p, a


#===================================
# Probability calculation functions
#===================================

def probability_greater_than() -> None:
    print("Calculating P(x > a)...")
    n, p, a = get_parameters()
    # Placeholder for actual calculation logic
    pass

def probability_greater_equal() -> None:
    print("Calculating P(x >= a)...")
    n, p, a = get_parameters()
    # Placeholder for actual calculation logic
    pass

def probability_less_than() -> None:
    print("Calculating P(x < a)...")
    n, p, a = get_parameters()
    # Placeholder for actual calculation logic
    pass

def probability_less_equal() -> None:
    print("Calculating P(x <= a)...")
    n, p, a = get_parameters()
    # Placeholder for actual calculation logic
    pass

def probability_equal() -> None:
    print("Calculating P(x = a)...")
    n, p, a = get_parameters()
    # Placeholder for actual calculation logic
    pass