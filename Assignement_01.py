# Q.1 Print HelloWorld
print("HelloWorld")
#=================================================================================
# Q.2 describe local variable and global variable code
x = "I am global"
def my_function():
    y = "I am local"
    print(x)
    print(y)
my_function()
#=================================================================================
# Q.3 Write a code that describe Indentation error
def my_function():
print("This will cause an IndentationError")
#==================================================================================

# Q.4 write a code that describe local and global variable with same name
x = 10
def my_function():
    x = 20
    print("Local x:", x)
my_function()
print("Global x:", x)
#===================================================================================

# Q.5  Write a code for string, int and float input.
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
print(f"Name: {name}, Age: {age}, Height: {height}m")
