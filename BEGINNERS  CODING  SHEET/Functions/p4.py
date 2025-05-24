#  Write a Program to Convert Decimal to Binary number manually by creating user-defined functions

def decimal_to_binary(decimal):
    if decimal == 0:
        return "0"
    binary = ""
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal //= 2
    return binary


decimal_number = int(input("Enter a decimal number: "))
binary_value = decimal_to_binary(decimal_number)
print(f"The binary value of decimal {decimal_number} is {binary_value}")
