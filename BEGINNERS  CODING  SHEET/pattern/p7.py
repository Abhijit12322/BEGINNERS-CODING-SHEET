# Hollow Full Pyramid Star

x = int(input("Enter number of rows: "))
for i in range(x):
    for j in range(x - i):
        print(" ", end=" ")
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i or i == x - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("")
