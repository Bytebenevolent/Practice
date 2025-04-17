# First example.
try:
    name = input("Enter your name: ").title()
    print(f"Hello, {name}")
    num_1 = int(input("Enter num 1: "))
    result = num_1 ** 2
    print(result)
except ValueError as value_error:
    print(f"Value error: {value_error}")
except ZeroDivisionError as math_error:
    print(f"Number error: {math_error}")

# Second example.
try:
    number = int(input("Enter number: "))
    if number != 0:
        result = number / 10
        print(result)
except ZeroDivisionError as math_error:
    print(f"Error! {math_error}")
except Exception as exception:
    print(exception)