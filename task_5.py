# Task 1.
while True:
    number = input('Number: ')
    integer = int(number)
    if integer is not None:
        print(integer)
    break

# Task 2.
try:
    with open('text.txt', 'r') as file:
        for line in file:
            try:
                result = float(line.strip())  
                print(result)
            except ValueError:
                print(f"Error: Failed to convert to '{line.strip()}' number.")
except FileNotFoundError:
    print("Error: File not found")
except Exception as exception:
    print(f"Unknown error: {exception}")


# Task 3.
try:
    with open('text.txt', 'r+') as file:
        for number in file:
            result = float(number)
            print(result)
except Exception as exception:
    print(f"Error: {exception}")
