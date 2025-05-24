#  Write a Program to Reverse a given Number N by user

x = int(input("Enter a number: "))

rev = 0
while x != 0:
    rev = rev * 10 + x % 10
    x = x // 10

print(f"The reverse of the number is {rev}")
