# Write a Program to Find GCD or HCF of two numbers entered by user

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))


for i in range(2, min(x, y) + 1):
    if (x % i == 0) and (y % i == 0):
        hcf = i

print(f"The GCD of {x} and {y} is {hcf}")
