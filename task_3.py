fullname = input("Enter your full name: ").title()
age = int(input("Enter your age: "))
total = age + 10
print(f"Hello, {fullname}! After ten years you'll be {total} years old")
if total >= 18:
    print("You're adult")
else:
    print("You're yuong")
