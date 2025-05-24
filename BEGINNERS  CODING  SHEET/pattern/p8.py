#  Half pyramid using numbers

x = int(input("Enter number of rows: "))
for i in range(x):
    for j in range(i + 1):
        print(j + 1, end=" ")
    print("")
