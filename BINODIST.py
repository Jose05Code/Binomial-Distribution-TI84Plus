import math as pymath
class ui:
    @staticmethod
    def menu():
        ui.clear()
        print("\n===============================")
        print("Welcome to the Bino Library")
        print("1. P(x > a)")
        print("2. P(x >= a)")
        print("3. P(x < a)")
        print("4. P(x <= a)")
        print("5. P(x = a)")
        print("===============================")

    @staticmethod
    def get_user_choice(number_of_choices):
        while True:
            prompt = "\nEnter your choice (1-{}): ".format(number_of_choices)
            choice = int(input(prompt))
            if choice < 1 or choice > number_of_choices:
                print("\nInvalid choice. Please enter a number between 1 and {}.".format(number_of_choices))
            else:
                return choice

    @staticmethod
    def clear():
        for i in range(20):
            print("")

    @staticmethod
    def print_answer(answer):
        ui.clear()
        print("The answer is: ", answer)
        input("Push enter to continue.")
            
    @staticmethod
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

    @staticmethod
    def probability_greater_than():
        print("\nCalculating P(x > a)...")
        n, p, a = ui.get_parameters()
        return 1-math.binocdf(n,p,a)

    @staticmethod
    def probability_greater_equal():
        print("\nCalculating P(x >= a)...")
        n, p, a = ui.get_parameters()
        return 1-math.binocdf(n,p,a-1)

    @staticmethod
    def probability_less_than():
        print("\nCalculating P(x < a)...")
        n, p, a = ui.get_parameters()
        return math.binocdf(n,p,a-1)

    @staticmethod
    def probability_less_equal():
        print("\nCalculating P(x <= a)...")
        n, p, a = ui.get_parameters()
        return math.binocdf(n,p,a)

    @staticmethod
    def probability_equal():
        print("\nCalculating P(x = a)...")
        n, p, a = ui.get_parameters()
        return math.binopdf(n,p,a)
        
class math:
    @staticmethod
    def nCr(n, a):
        if a < 0 or a > n:
            return 0
        return pymath.factorial(n) // (pymath.factorial(a) * pymath.factorial(n - a))

    @staticmethod
    def binopdf(n, p, a):
        return math.nCr(n, a)*(p**a)*(1-p)**(n-a)

    @staticmethod
    def binocdf(n, p, a):
        cdf = 0
        for i in range(a+1):
            cdf += math.binopdf(n,p,i)
        return cdf

def main():
    switcher = {
        1: ui.probability_greater_than,
        2: ui.probability_greater_equal,
        3: ui.probability_less_than,
        4: ui.probability_less_equal,
        5: ui.probability_equal,
    }
    max_option = max(switcher.keys())
    while True:
        ui.menu()
        choice = ui.get_user_choice(max_option)
        func = switcher.get(choice)
        ui.print_answer(func())

main()