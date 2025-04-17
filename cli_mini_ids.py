def analyze_attempt(login, password, dangerous_passwords):
    if len(password) < 8:
        print(f"{login}: Weak password")
        return 'weak'
    elif password in dangerous_passwords:
        print(f"{login}: Common password")
        return 'common'
    else:
        print(f"{login}: Accepted")
        return 'accepted'


dangerous_passwords = ['123456', 'qwerty', 'letmein', 'admin123']

attempts_list = [
    {'login': 'admin', 'password': '123456'},
    {'login': 'user1', 'password': 'qwerty'},
    {'login': 'root', 'password': 'letmein'},
    {'login': 'guest', 'password': 'admin123'},
    {'login': 'neo', 'password': 'Matrix2024'}
]

weak_count = 0
common_count = 0
accepted_count = 0

for attempt in attempts_list:
    login = attempt['login']
    password = attempt['password']
    result = analyze_attempt(login, password, dangerous_passwords)

    if result == 'weak':
        weak_count += 1
    elif result == 'common':
        common_count += 1
    elif result == 'accepted':
        accepted_count += 1

print("\n--- Summary ---")
print(f"Total: {len(attempts_list)}")
print(f"Weak: {weak_count}")
print(f"Common: {common_count}")
print(f"Accepted: {accepted_count}")
