# 1. Print the table of 5 using a for loop.
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")
#==================================================================

# 2. Print even number series by taking input from the user.
limit = int(input("Enter the limit for even numbers: "))
for i in range(2, limit + 1, 2):
    print(i, end=" ")
print()
#==================================================================

# 3. Create a list and iterate through its items using a for loop.
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(f"Item: {item}")
#==================================================================

# 4. Calculate the sum of numbers from 1 to 10.
total_sum = sum(range(1, 11))
print(f"The sum of numbers from 1 to 10 is: {total_sum}")
#==================================================================

''' 5. Print the given pattern.
          *

         ***

       *****

      *******

     ********* '''

rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
#==================================================================

# 6. Print the first 10 natural numbers using a for loop.
for i in range(1, 11):
    print(i, end=" ")
print()
#==================================================================

# 7. Python program to check if the given string is a palindrome.
string = input("Enter a string: ")
if string == string[::-1]:
    print(f"The string '{string}' is a palindrome.")
else:
    print(f"The string '{string}' is not a palindrome.")
#==================================================================

# 8. Python program to check if a given number is an Armstrong number.
number = int(input("Enter a number: "))
original_number = number
num_digits = len(str(number))
sum_of_powers = sum(int(digit) ** num_digits for digit in str(number))

if sum_of_powers == original_number:
    print(f"The number {original_number} is an Armstrong number.")
else:
    print(f"The number {original_number} is not an Armstrong number.")
#==================================================================

# 9. Python program to get the Fibonacci series between 0 to 50.
a, b = 0, 1
print("Fibonacci series between 0 to 50:")
while a <= 50:
    print(a, end=" ")
    a, b = b, a + b
print()
#==================================================================

# 10. Python program to check the validity of password input by users.
import re
password = input("Enter a password: ")
if (len(password) >= 8 and
    re.search(r"[A-Z]", password) and
    re.search(r"[a-z]", password) and
    re.search(r"[0-9]", password) and
    re.search(r"[@$!%*?&#]", password)):
    print("Valid password!")
else:
    print("Invalid password. Make sure it meets the criteria.")

#==================================================================

# 1. Program to print the factorial of a number.
number = int(input("Enter a number to find its factorial: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"The factorial of {number} is: {factorial}")
#==================================================================

# 2. Program to check whether the given number is prime or not.
number = int(input("Enter a number to check if it is prime: "))
is_prime = True
if number > 1:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"The number {number} is a prime number.")
    else:
        print(f"The number {number} is not a prime number.")
else:
    print(f"The number {number} is not a prime number.")
#==================================================================

'''3. Program to display the patterns.
1

1 2

1 2 3

1 2 3 4

1 2 3 4 5



A

B C

D E F

G H I J K

L M N O P Q



         *

       ***

      *****

     *******

'''

# Pattern 1:
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
print()


# Pattern 2:
letters = iter("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print(next(letters), end=" ")
    print()
print()


# Pattern 3:
rows = 4
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
print()

