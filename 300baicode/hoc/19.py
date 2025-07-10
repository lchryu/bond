a , b , c = map (int , input ().split())
d = a // 2
if a % 2 == 1 :
    d = d + 1
n = b // 2
if b % 2 == 1 :
    n = n + 1
m =  c // 2
if c % 2 == 1 :
    m = m + 1
y = m + n + d
print (y)