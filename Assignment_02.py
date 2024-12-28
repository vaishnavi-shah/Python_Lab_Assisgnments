# Q.1 Write a program for arithmatic operators
a = 10
b = 5
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("Floor Division:", a // b)
#============================================================
# Q.2 Write a program for assignment operators
a = 10
a = 5
print("Assigned value:", a)

a += 3
print("After += 3:", a)

a -= 2
print("After -= 2:", a)

a *= 4
print("After *= 4:", a)

a /= 2
print("After /= 2:", a)

a %= 3
print("After %= 3:", a)

a **= 2
print("After **= 2:", a)

a //= 2
print("After //= 2:", a)
#=================================================================

# Q.3 Write a program for Bitwise Operators
a = 5   # Binary: 0101
b = 3   # Binary: 0011
print("AND:", a & b)
print("OR:", a | b)
print("XOR:", a ^ b)
print("NOT:", ~a)
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)
#===================================================================

# Q.4 Write a program to calculate greatest of three numbers.
a = 10
b = 20
c = 15
greatest = a if a > b and a > c else b if b > c else c
print("The greatest number is:", greatest)

#=====================================================================

# 1. Calculate the Area of a Circle
radius = float(input("Enter the radius of the circle: "))
area_circle = 3.14159 * radius ** 2
print("Area of the circle:", area_circle)
#=====================================================================

# 2. Calculate the Area of a Triangle
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area_triangle = 0.5 * base * height
print("Area of the triangle:", area_triangle)
#======================================================================

# 3. Calculate the Area of a Rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area_rectangle = length * width
print("Area of the rectangle:", area_rectangle)
#=======================================================================

# 4. Calculate the Area of a Square
side = float(input("Enter the side length of the square: "))
area_square = side ** 2
print("Area of the square:", area_square)



