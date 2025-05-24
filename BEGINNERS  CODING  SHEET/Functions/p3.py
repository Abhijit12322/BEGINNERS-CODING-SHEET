# Write a Program to Convert Binary Number to Decimal manually by creating user-defined functions

def binary_to_decimal(binary_str):
    decimal = 0
    power = 0
    for digit in reversed(binary_str):
        if digit == '1':
            decimal += 2 ** power
        power += 1
    return decimal


binary_str = input("Enter a binary number: ")
decimal_value = binary_to_decimal(binary_str)
print(f"The decimal value of binary {binary_str} is {decimal_value}")
