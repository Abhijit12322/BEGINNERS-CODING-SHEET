#  Inverted Full pyramid

x = int(input("Enter number of rows: "))
for i in range(x):
    for j in range(i):
        print(" ", end=" ")
    for j in range(2 * (x - i) - 1):
        print("*", end=" ")
    print("")
