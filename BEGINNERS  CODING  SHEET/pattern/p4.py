#  Inverted Half pyramid

x = int(input("Enter number of rows: "))
for i in range(x):
    for j in range(x - i):
        print("*", end=" ")
    print("")
