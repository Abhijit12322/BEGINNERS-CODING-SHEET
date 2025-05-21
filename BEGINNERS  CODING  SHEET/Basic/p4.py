x = int(input("Enter a divisor: "))
y = int(input("Enter a divident: "))

c = y % x
d = int(y / x)

print(f"The remainder of the two numbers {x} and {y} is: ", c)
print(f"The quotient of the two numbers {x} and {y} is: ", d)
