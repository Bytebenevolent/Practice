full_name = input("Enter your first name: ").title()
year_of_birth = int(input("Enter your year of birth: "))
# Conditionals(if-elif-else).
if full_name == "Robert De Niro" and year_of_birth == 1_943:
    print("You're an actor")
elif full_name == "Kelly Clarkson" and year_of_birth == 1_982:
    print("You're a singer")
elif full_name == "Kazuya Mishima" and year_of_birth ==  1_967:
    print("you're a character from the game Tekken")
else: 
    print("I don't know")