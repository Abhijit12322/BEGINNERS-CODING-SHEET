# Write a Program to Display Prime Numbers BetweenTwo Intervals  (entered by user)
# Example:Enter two numbers: 0 20
# Prime numbers between 0 and 20 are:2 3 5 7 11 13 17 19

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

print(f"Prime numbers between {x} and {y} are: ", end="")
for num in range(x, y + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
