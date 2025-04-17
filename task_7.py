# Task 1.
safe_passwords = ["secure123_secure", "my_password", 'password202']

while True:
    user_password = input("Enter safely password: ")

    if user_password in safe_passwords: 
        print('Correct')
        break
    else:
        print("Dangerous password")

# Task 2.
for number in range(50):
    if number % 2 == 0:
        print('Even')
    else:
        print('Odd')

# Task 3.
text = input("Enter some text: ")
reversed_text = ''
index = len(text) - 1

while index >= 0:
    reversed_text += text[index]
    index -= 1
print("Reversed text:", reversed_text)