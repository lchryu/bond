def s(a):
    b = 0
    while a > 0 :
        b += a % 10
        a //= 10
    return b
if __name__ == '__main__':
    list_input = list(map(int, input().split()))
    list_input2 = list(map(s, list_input))
    for x, y in zip(list_input, list_input2):
        print(x, y)