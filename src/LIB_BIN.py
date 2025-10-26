import LIB_MATH as math

def menu():
    clear()
    print("\n===============================")
    print("Welcome to the Bino Library")
    print("1. P(x > a)")
    print("2. P(x >= a)")
    print("3. P(x < a)")
    print("4. P(x <= a)")
    print("5. P(x = a)")
    print("===============================")

def get_user_choice(number_of_choices):
    while True:
        prompt = "\nEnter your choice (1-{}): ".format(number_of_choices)
        choice = int(input(prompt))
        if choice < 1 or choice > number_of_choices:
            print("\nInvalid choice. Please enter a number between 1 and {}.".format(number_of_choices))
        else:
            return choice
        
def clear():
    for i in range(20):
        print("")
        
def print_answer(answer):
    clear()
    print("The answer is: ", answer)
    input("Push enter to continue.")

def get_values(value_type, text, condition, error_message, expect_error):
    while True:
        try:
            value = value_type(input(text))
            if not condition(value):
                print(error_message)
                continue
            return value
        except ValueError:
            print(f"\n{expect_error}")

def get_parameters():
    n = get_values(
        int,
        "\nEnter the number of trials (n >= 0): ",
        lambda x: x >= 0,
        "\nNumber of trials must be a non-negative integer.",
        "\nInvalid input. Please enter a non-negative integer for n."
    )
    p = get_values(
        float,
        "\nEnter the probability of success in decimal (0 <= p <= 1): ",
        lambda x: 0 <= x <= 1,
        "\nProbability must be between 0 and 1 (inclusive).",
        "\nInvalid input. Please enter a decimal number between 0 and 1 for p."
    )
    a = get_values(
        int,
        "\nEnter the value of a (a >= 0): ",
        lambda x: x >= 0,
        "\nValue of a must be a non-negative integer.",
        "\nInvalid input. Please enter a non-negative integer for a."
    )
    return n, p, a


#===================================
# Probability calculation functions
#===================================

def probability_greater_than():
    print("\nCalculating P(x > a)...")
    n, p, a = get_parameters()
    return 1-math.binocdf(n,p,a)

def probability_greater_equal():
    print("\nCalculating P(x >= a)...")
    n, p, a = get_parameters()
    return 1-math.binocdf(n,p,a-1)

def probability_less_than():
    print("\nCalculating P(x < a)...")
    n, p, a = get_parameters()
    return math.binocdf(n,p,a-1)

def probability_less_equal():
    print("\nCalculating P(x <= a)...")
    n, p, a = get_parameters()
    return math.binocdf(n,p,a)

def probability_equal():
    print("\nCalculating P(x = a)...")
    n, p, a = get_parameters()
    return math.binopdf(n,p,a)