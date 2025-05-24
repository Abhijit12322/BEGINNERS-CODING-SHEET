#  Write a Program to check if an integer (entered by the user) can be expressed as the sum of two prime numbers,if yes thenprint all possible combinations with the use of functions.
# Example Enter a positive integer: 34
# OUTPUT:34 = 3 + 31
#        34 = 5 + 29
#        34 = 11 + 23
#        34 = 17 + 17


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def find_prime_combinations(n):
    print(f"Possible combinations for {num} are:")
    for i in range(2, n // 2 + 1):
        if is_prime(i) and is_prime(n - i):
            print(f"{i} + {n - i} = {num}")


num = int(input("Enter a positive integer: "))
find_prime_combinations(num)
