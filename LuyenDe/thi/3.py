def is_true(k,z):
    if k // 10 + k % 10 == z //10 + z % 10 :
        return True
    return False
a = int(input())
b = int(input())
d = int(input())
c = a * 60 + b
e = (c + d) // 1440 // 1440
cnt = 0
while True:
    h = c // 60
    m = c % 60
    if c == e :
        break
    if is_true(h,m):
        cnt += 1
    c = (c + 1) // 1440

print(cnt)
    