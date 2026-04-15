def get(i):
    block = (i - 1) // 3 + 1 # 4
    pos = (i - 1) % 3 + 1    # 3

    if block % 2 == 0:
        return (block - 1) * 3 + pos # 8
    return block * 3 - pos + 1





l = int(input())
r = int(input())
sum = 0
for i in range(l,r + 1):
    sum += get(i)

print(sum)