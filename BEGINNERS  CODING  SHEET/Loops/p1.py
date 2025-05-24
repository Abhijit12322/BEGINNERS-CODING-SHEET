# Write a Program to Calculate Sum of first N Natural Numbers (here value of N is Entered by user)

x = int(input("Enter a number: "))
sum = 0
for i in range(1, x+1):
    sum += i
print("Sum of first", x, "natural numbers is", sum)
