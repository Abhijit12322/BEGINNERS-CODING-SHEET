#  Write a Program to display sum of all digits of a given Number N by user

x = int(input("Enter a number: "))
sum = 0
while x > 0:
    digit = x % 10
    sum += digit
    x = x//10
print("Sum of digits is:", sum)
