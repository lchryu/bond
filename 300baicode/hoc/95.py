def sum_digit (n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

def raw_number(n):
    while n >= 10:
        n = sum_digit(n)
    return n
n = int(input())
print(raw_number(n))  # Output: 15

