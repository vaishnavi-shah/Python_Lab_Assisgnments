# 1. Declare a div() function with two parameters. Then call the function and pass two numbers and display their division.
def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print(f"The division of {num1} and {num2} is: {div(num1, num2)}")
#=====================================================================================================================

# 2. Declare a square() function with one parameter. Then call the function and pass one number and display the square of that number.
def square(a):
    return a ** 2
num = float(input("Enter a number to find its square: "))
print(f"The square of {num} is: {square(num)}")
#======================================================================================================================

# 3. Using max() and min() functions display the maximum and minimum of 5 random numbers.
import random
random_numbers = [random.randint(1, 100) for _ in range(5)]
print(f"The 5 random numbers are: {random_numbers}")
print(f"The maximum number is: {max(random_numbers)}")
print(f"The minimum number is: {min(random_numbers)}")
#======================================================================================================================

# 4. Accept a name from the user and display that in lower case using lower() function
name = input("Enter your name: ")
print(f"Your name in lower case is: {name.lower()}")
