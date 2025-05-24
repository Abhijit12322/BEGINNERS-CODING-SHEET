#  Write a Program to check whether a number entered by the user is an Armstrong number or not

x = int(input("Enter a number: "))
sum = 0
temp = x
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if sum == x:
    print(f"{x} is an Armstrong number.")
else:
    print(f"{x} is not an Armstrong number.")
