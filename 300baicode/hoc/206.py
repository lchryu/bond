
s = input()
x = input()
n = int(input())



total_padding = n - len(s)

left_padding = total_padding // 2
right_padding = total_padding // 2

if total_padding % 2 != 0:
    if n % 2 != 0:
        left_padding += 1
    else:
        right_padding += 1


result = (x * left_padding) + s + (x * right_padding)
print(result)



