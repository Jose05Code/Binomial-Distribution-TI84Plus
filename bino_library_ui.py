def menu() -> None:
    """Display the main menu to the user."""

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
    """
    Get a valid user choice from the menu.

    Args:
        number_of_choices (int): The maximum valid menu option value (inclusive). Valid choices are integers from 0 to number_of_choices, inclusive.

    Returns:
        int: The user's valid choice (between 0 and number_of_choices, inclusive).
    """

    while True:
        choice = int(input(f"Enter your choice (0-{number_of_choices}): "))
        if choice < 0 or choice > number_of_choices:
            print(f"Invalid choice. Please enter a number between 0 and {number_of_choices}.")
        else:
            return choice
        
def get_parameters() -> tuple[int, float, int]:
    """
    Prompt the user for parameters n, p, and a.

    Returns:
        tuple: A tuple containing (n, p, a).
    """
    n = int(input("Enter the number of trials (n): "))
    p = float(input("Enter the probability of success in decimal (p): "))
    a = int(input("Enter the value of a: "))
    return n, p, a


#===================================
# Probability calculation functions
#===================================

def probability_greater_than() -> None:
    """Calculate the probability P(x > a)."""
    print("Calculating P(x > a)...")
    n, p, a = get_parameters()
    # Placeholder for actual calculation logic
    pass

def probability_greater_equal() -> None:
    """Calculate the probability P(x >= a)."""
    print("Calculating P(x >= a)...")
    n, p, a = get_parameters()
    # Placeholder for actual calculation logic
    pass

def probability_less_than() -> None:
    """Calculate the probability P(x < a)."""
    print("Calculating P(x < a)...")
    n, p, a = get_parameters()
    # Placeholder for actual calculation logic
    pass

def probability_less_equal() -> None:
    """Calculate the probability P(x <= a)."""
    print("Calculating P(x <= a)...")
    n, p, a = get_parameters()
    # Placeholder for actual calculation logic
    pass

def probability_equal() -> None:
    """Calculate the probability P(x = a)."""
    print("Calculating P(x = a)...")
    n, p, a = get_parameters()
    # Placeholder for actual calculation logic
    pass