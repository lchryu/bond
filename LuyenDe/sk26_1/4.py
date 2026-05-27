a = int(input())
b = int(input())
c = int(input())
d = int(input())
cur = a * 60 + b
end = c * 60 + d
t = 0

while True:
    h = cur //60
    m = cur % 60
    t = t + (str(h) + str(m)).count("2")
    if cur == end : break
    cur = (cur + 1 ) % 1440
print(t)    
    