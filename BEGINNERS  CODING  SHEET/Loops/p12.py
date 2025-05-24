# Write a Program to Check Whether a number N entered by user is palindrome or not

x = int(input("Enter a number: "))
temp = x
rev = 0
while x != 0:
    rev = rev * 10 + x % 10
    x //= 10
if temp == rev:
    print(f"{temp} is a palindrome")
else:
    print(f"{temp} is not a palindrome")
