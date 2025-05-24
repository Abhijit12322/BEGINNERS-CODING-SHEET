# Write a Program to Display Fibonacci Series upto nth term (n is entered by user).

n = int(input("Enter the number of terms: "))
print("Fibonacci Series:- ")

a = 0
b = 1
for i in range(n):
    print(a)
    c = a+b
    a = b
    b = c
