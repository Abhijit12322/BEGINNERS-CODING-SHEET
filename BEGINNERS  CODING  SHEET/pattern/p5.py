# Full Pyramid Star Pattern

x = int(input("Enter number of rows: "))
for i in range(x):
    for j in range(x - i):
        print(" ", end=" ")
    for j in range(2 * i + 1):
        print("*", end=" ")
    print("")
