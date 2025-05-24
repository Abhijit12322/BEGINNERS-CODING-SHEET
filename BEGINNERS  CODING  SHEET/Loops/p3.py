#  Write a Program to Generate Multiplication Table of a number (entered by the user) using a for loop.

x = int(input("Enter a number: "))
print(f"Multiplication Table of {x}:- ")

for i in range(1, 11):
    print(f"\t {x} x {i} = {x*i}")
