# Write a Program to Calculate Power of a Number without using inbuilt pow() function by taking two inputs from users as Base and exponent respectively

x = int(input("Enter the base number: "))
y = int(input("Enter the exponent number: "))

result = 1
for i in range(y):
    result *= x
print(f"{x} raised to the power of {y} is: {result}")
