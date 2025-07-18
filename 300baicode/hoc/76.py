def sum_even(a , b):
    total = 0
    for i in range(a, b + 1):
        if i % 2 == 0:
            total += i
    return total

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(sum_even(a, b))