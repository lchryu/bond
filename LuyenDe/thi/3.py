def is_true(k,z):
    return k // 10 + k % 10 == z //10 + z % 10
a = int(input())
b = int(input())
d = int(input())
c = a * 60 + b
# e = (c + d) // 1440 // 1440
e = (c + d) % 1440
cnt = 0
while True:
    h = c // 60
    m = c % 60
    if is_true(h,m):
        cnt += 1
    if c == e :
        break
    c = (c + 1) % 1440

print(cnt)
    

