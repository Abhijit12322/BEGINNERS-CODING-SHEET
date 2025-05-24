# Write a Program to Check Whether a Number is Prime or Not

x = int(input("Enter a number: "))

flag = 0
for i in range(2, x):
    if x % i == 0:
        flag = 1
        break
    else:
        flag = 0

if flag == 0:
    print(f"{x} is a prime number")
else:
    print(f"{x} is not a prime number")
