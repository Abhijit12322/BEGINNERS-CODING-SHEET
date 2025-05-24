# Write a Program to Calculate Power of a Number using in built pow() function by taking two inputs from users as Base and exponent respectively

x = int(input("Enter the base number: "))
y = int(input("Enter the exponent number: "))

result = pow(x, y)
print(f"{x} raised to the power of {y} is: {result}")
