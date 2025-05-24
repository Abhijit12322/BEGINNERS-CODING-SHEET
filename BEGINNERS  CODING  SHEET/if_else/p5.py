# Write a Program to Check whether a year entered by user is Leap Year or not

x = int(input("Enter a year: "))

if (x % 4 == 0):
    print(x, "is a leap year")
else:
    print(x, "is not a leap year")
