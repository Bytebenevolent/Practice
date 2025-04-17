try:
    number_1 = int(input("Enter first number: "))
    operator = input("Choose operator(+ - * /): ") 
    number_2 = int(input("Enter second number: ")) 
    if operator == '+':
        result = number_1 + number_2
    elif operator == '-':
        result = number_1 - number_2
    elif operator == '*':
        result = number_1 * number_2
    elif operator == '/':
        result = number_1 / number_2
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError as value_error:
    print(f"Value error: {value_error}")
except Exception as exception:
    print(f"Unknown error: {exception}")