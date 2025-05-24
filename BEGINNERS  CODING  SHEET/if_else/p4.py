# Write a Program which accepts coefficients of a quadratic equation from the user and displays the roots (both real and complex roots depending upon the discriminant).

x = float(input("Enter coefficient a: "))
y = float(input("Enter coefficient b: "))
z = float(input("Enter coefficient c: "))

d = y**2 - 4*x*z

if d > 0:
    root1 = (-y + d**0.5) / (2*x)
    root2 = (-y - d**0.5) / (2*x)
    print(f"The roots are real and different: {root1} and {root2}")
elif d == 0:
    root = -y / (2*x)
    print(f"The roots are real and the same: {root}")
else:
    real_part = -y / (2*x)
    imaginary_part = (-d)**0.5 / (2*x)
    print(
        f"The roots are complex: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i")
