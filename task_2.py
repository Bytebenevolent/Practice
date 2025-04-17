password_input = 'admin123'
wordlist = ['123456', 'letmein', 'qwerty', 'admin123', 'passw0rd']

for password in wordlist:
    print(f"Attemt: {password}")
    if password == password_input:
        print(f"Correct password: {password}")
        break
else:
    print("Password not found")