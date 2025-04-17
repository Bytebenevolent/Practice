dangerous_passwords = ['qwerty', 'password', 'dragon']

while True:
    password = input("Enter security password: ")
    if password not in dangerous_passwords and len(password) >= 8:
        print("Password accepted")
        break
    else:
        print("The password is too obvious")