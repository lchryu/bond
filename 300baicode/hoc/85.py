def sum_digits(n):
    a = 0
    while n > 0 :
        a += n % 10
        n //= 10
    return a

if __name__ == '__main__':
    n = int(input())
    print(sum_digits(n))