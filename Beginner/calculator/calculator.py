import math
import sys


def add(x, y):  # Liitmine

    return x + y


def subtract(x, y):  # Lahutamine
    return x - y


def multiply(x, y):  # Korrutamine
    return x * y


def divide(x, y):  # Jagamine
    if y == 0:
        raise ValueError(" No 0 !")
    return x / y


def power(x, y):  # Astendamine
    return x**y


def square_root(x):  # Ruutfunktsioon
    if x < 0:
        raise ValueError("No Negatives!")
    return math.sqrt(x)


def display_menu():  # Menüü kuvamine
    print("\n" + "=" * 50)
    print("    Simple Calculator")
    print("=" * 50)
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Square Root (√)")
    print("7. Exit")
    print("=" * 50)


def get_number(prompt):  # inputi kontrollimine
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def get_choice():  # Kasutaja valiku kontrollimine
    while True:
        try:
            choice = int(input("Enter choice (1-7): "))
            if choice in range(1, 8):
                return choice
            else:
                print("Invalid choice! Please select 1-7.")
        except ValueError:
            print("Invalid input! Please enter a number 1-7.")


def main():  # Põhi programm
    print("Welcome to Simple Calculator!")
    print("Type numbers when prompted and select operations from the menu.")

    while True:
        display_menu()
        choice = get_choice()

        if choice == 7:
            print("\n Thank you for using Simple Calculator!")
            print("Goodbye!")
            sys.exit()

        try:
            if choice == 6:  # vajab ainult ühte numbrit
                num = get_number("Enter number: ")
                result = square_root(num)
                print(f"\n √{num} = {result:.4f}")

            else:  # vajab kahte numbrit
                num1 = get_number("Enter first number: ")
                num2 = get_number("Enter second number: ")

                if choice == 1:
                    result = add(num1, num2)
                    print(f"\n {num1} + {num2} = {result}")

                elif choice == 2:
                    result = subtract(num1, num2)
                    print(f"\n {num1} - {num2} = {result}")

                elif choice == 3:
                    result = multiply(num1, num2)
                    print(f"\n {num1} × {num2} = {result}")

                elif choice == 4:
                    result = divide(num1, num2)
                    print(f"\n {num1} ÷ {num2} = {result:.4f}")

                elif choice == 5:
                    result = power(num1, num2)
                    print(f"\n {num1} ^ {num2} = {result}")

        except ValueError as error:
            print(f"\n Error: {error}")
        except Exception as error:
            print(f"\n Unexpected error: {error}")

        # küsimine, kas kasutaja soovib jätkata
        print("\n" + "-" * 50)
        continue_calc = input(
            "Do you want to perform another calculation? (y/n): "
        ).lower()
        if continue_calc not in ["y", "yes"]:
            print("\n Thank you for using Simple Calculator!")
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
