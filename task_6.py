name = input("Enter your name: ").title()
age = int(input("Enter your age: "))
programming_languages = input("Enter your favorite programming languages: ").title().strip()

data = programming_languages.split(',')
my_set = set(data)
my_dict = {
    'name': name,
    'age': age,
    'langs': programming_languages
}
print(f"Name: {name}, age: {age}, my_langs: {list(programming_languages)}")