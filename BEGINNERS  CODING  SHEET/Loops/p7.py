# Write a Program to Find LCM of two numbers entered by user

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

gcd = 1
for i in range(1, min(x, y) + 1):
    if (x % i == 0) and (y % i == 0):
        gcd = i
print(f"The LCM of {x} and {y} is {int((x * y)/gcd)}")
