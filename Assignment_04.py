# 1. Write a Python program that takes a number as input and prints "Even" if the number is even and "Odd" if it's odd.
number = int(input("Enter a number: "))
result = "Even" if number % 2 == 0 else "Odd"
print(f"The number {number} is {result}.")
#==================================================================================================================

# 2. Create a Python program that checks whether a person is eligible to vote (18 years or older) based on their age.
age = int(input("Enter your age: "))
eligibility = "Eligible to vote" if age >= 18 else "Not eligible to vote"
print(eligibility)
#===================================================================================================================

# 3. Write a Python program that determines if a given year is a leap year or not.
year = int(input("Enter a year: "))
is_leap_year = "Leap year" if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) else "Not a leap year"
print(f"{year} is {is_leap_year}.")
#===================================================================================================================

# 4. Create a Python program that checks if a user-given number is positive, negative, or zero.
number = float(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
#===================================================================================================================

# 5. Write a Python program that determines the largest of three numbers entered by the user.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
largest = max(num1, num2, num3)
print(f"The largest number is {largest}.")
