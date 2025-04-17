# Task 1.
def get_sum(x, y):
    result = x + y
    return result


get_sum(25, 60)

# Task 2.
def get_the_number_of_vowels(word):
    vowels = 'aeiouAEIOU'
    count = 0

    for char in word:
        if char in vowels:  
            count += 1
    return count



# Task 3.
def get_number(a):
    if a % 2 == 0:
        print(f"{a}'s even")
    else: 
        print(f"{a}'s odd")


get_number(5)

# Task 4.
def get_max_value(a, b, c):
    values = a, b, c
    print(max(values))


get_max_value(100, 25, 1)

# Task 5.
def find_letter(text):
    vowels = 'aeiouAEIOU'  # Vowel letters.
    max_vowel = '' 
    
    for char in text:
        if char in vowels:  #
            if char > max_vowel: 
                max_vowel = char 
    return max_vowel
