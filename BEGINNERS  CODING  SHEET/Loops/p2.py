# Write a Program to Find Factorial of a given number N (N is entered by user)

x = int(input("Enter the No: "))

no = 1
print(f"The Factorial of {x} is")
for i in range(1, x+1):
    if x % i == 0:
        print("\t", i)
