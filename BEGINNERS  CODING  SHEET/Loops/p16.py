#  Write a Program to Display all Factors of a Number entered by User

x = int(input("Enter a number: "))
print(f"Factors of {x} are: ")
for i in range(1, x + 1):
    if x % i == 0:
        print(i)
