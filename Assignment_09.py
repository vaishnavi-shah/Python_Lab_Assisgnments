# 1. Write a Python program to count all letters, digits, and special symbols from the given string.
input_string = "P@#yn26at^&i5ve"
chars, digits, symbols = 0, 0, 0
for char in input_string:
    if char.isalpha():
        chars += 1
    elif char.isdigit():
        digits += 1
    else:
        symbols += 1
print(f"Chars = {chars}, Digits = {digits}, Symbols = {symbols}")
#==================================================================

# 2. Write a Python program to remove duplicate characters of a given string.
input_string = "String and String Function"
output_string = " ".join(["".join(dict.fromkeys(word)) for word in input_string.split()])
print("Output:", output_string)
#==================================================================

# 3. Write a Python program to count Uppercase, Lowercase, special character, and numeric values in a given string.
input_string = "Hell0 W0rld ! 123 * # welcome to pYtHoN"
uppercase, lowercase, numbers, specials = 0, 0, 0, 0
for char in input_string:
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1
    elif char.isdigit():
        numbers += 1
    else:
        specials += 1
print(f"UpperCase: {uppercase}, LowerCase: {lowercase}, NumberCase: {numbers}, SpecialCase: {specials}")
#==================================================================

# 4. Write a Python program to count vowels in a string.
input_string = "Welcome to Python Assignment"
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in input_string if char in vowels)
print("Total vowels are:", vowel_count)

