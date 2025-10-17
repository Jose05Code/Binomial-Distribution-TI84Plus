import LIB_MATH as math

def menu():
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
        
def print_answer(answer):
    print("The answer is: ", answer)
    input("Push enter to continue.")
        
def get_parameters():
    while True:
        try:
            n = int(input("\nEnter the number of trials (n >= 0): "))
            if n < 0:
                print("\nNumber of trials must be a non-negative integer.")
                continue
            break
        except ValueError:
            print("\nInvalid input. Please enter a non-negative integer for n.")
    while True:
        try:
            p = float(input("\nEnter the probability of success in decimal (0 <= p <= 1): "))
            if p < 0 or p > 1:
                print("\nProbability must be between 0 and 1 (inclusive).")
                continue
            break
        except ValueError:
            print("\nInvalid input. Please enter a decimal number between 0 and 1 for p.")
    while True:
        try:
            a = int(input("\nEnter the value of a (a >= 0): "))
            if a < 0:
                print("\nValue of a must be a non-negative integer.")
                continue
            break
        except ValueError:
            print("\nInvalid input. Please enter a non-negative integer for a.")
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