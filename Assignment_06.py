# 1. Write a python program to reverse a number using a while loop.
number = int(input("Enter a number to reverse: "))
reversed_number = 0
while number != 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number = number // 10
print(f"The reversed number is: {reversed_number}")
#==================================================================

# 2. Write a python program to check whether a number is palindrome or not.
number = int(input("Enter a number to check if it is palindrome: "))
original_number = number
reversed_number = 0
while number != 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number = number // 10
if original_number == reversed_number:
    print(f"The number {original_number} is a palindrome.")
else:
    print(f"The number {original_number} is not a palindrome.")
#==================================================================

# 3. Write a python program finding the factorial of a given number using a while loop.
number = int(input("Enter a number to find its factorial: "))
factorial = 1
while number > 0:
    factorial *= number
    number -= 1
print(f"The factorial is: {factorial}")
#==================================================================

# 4. Accept numbers using input() function until the user enters 0. If user input 0 then break the while loop and display the sum of all the numbers.
total_sum = 0
while True:
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        break
    total_sum += number
print(f"The total sum is: {total_sum}")
#==================================================================

# 1. Program to check whether the given number is palindrome or not.
# Already covered in task 2.
#==================================================================

# 2. Program to check whether the given number is Armstrong or not.
number = int(input("Enter a number to check if it is Armstrong: "))
original_number = number
num_digits = len(str(number))
sum_of_powers = 0
while number > 0:
    digit = number % 10
    sum_of_powers += digit ** num_digits
    number = number // 10
if sum_of_powers == original_number:
    print(f"The number {original_number} is an Armstrong number.")
else:
    print(f"The number {original_number} is not an Armstrong number.")
#==================================================================

# 3. Program to find the factorial of a number.
# Already covered in task 3.
