# Write a Program to Make a Simple Calculator to Add, Subtract, Multiply or Divide Using Switch case
# The program should takes an arithmetic operator (+, -, *, /) and two operands from a user and performs the operation on those two operands depending upon the operator entered by the user.

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

op = input("Enter operator (+, -, *, /): ")
if op == '+':
    print(f"Result: {x} + {y} = {x + y}", end="")
elif op == '-':
    print(f"Result: {x} - {y} = {x - y}", end="")
elif op == '*':
    print(f"Result: {x} * {y} = {x * y}", end="")
elif op == '/':
    if y != 0:
        print(f"Result: {x} / {y} = {x / y}", end="")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operator. Please enter one of +, -, *, /.")
