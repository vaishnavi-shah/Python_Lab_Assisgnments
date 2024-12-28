# 1. Using input() function take one number from the user and using ternary operators check whether the number is even or odd
number = int(input("Enter a number: "))
result = "Even" if number % 2 == 0 else "Odd"
print(f"The number {number} is {result}.")
#===================================================================================================================

# 2.  Using input function take two number and then swap the number 
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num1, num2 = num2, num1
print(f"After swapping, first number is {num1} and second number is {num2}.")
#====================================================================================================================

# 3. Write a Program to Convert Kilometers to Miles 
kilometers = float(input("Enter distance in kilometers: "))
miles = kilometers * 0.621371
print(f"{kilometers} kilometers is equal to {miles} miles.")
#===================================================================================================================

# 4. Find the Simple Interest on Rs. 200 for 5 years at 5% per year.
principal = 200
rate_of_interest = 5
time = 5
simple_interest = (principal * rate_of_interest * time) / 100
print(f"The simple interest is Rs. {simple_interest}.")
