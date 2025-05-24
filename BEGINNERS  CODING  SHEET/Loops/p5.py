# Write a Program to Display Fibonacci Series upto certain number n (n is entered by user)
# Example: n=100
# Output:
# Fibonacci Series: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,

n = int(input("Enter the number of terms: "))
print("Fibonacci Series:- ")

a = 0
b = 1
for i in range(n):
    print(a)
    c = a+b
    a = b
    b = c
