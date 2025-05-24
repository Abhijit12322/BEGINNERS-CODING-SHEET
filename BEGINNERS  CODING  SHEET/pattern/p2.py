#  Hollow Rectangular star

x = int(input("Enter number of rows: "))
y = int(input("Enter number of columns: "))
for i in range(x):
    for j in range(y):
        if i == 0 or i == x - 1 or j == 0 or j == y - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("")
