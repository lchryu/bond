
a = int(input())
b = int(input())
s = a + 1
e = b - 1
if s % 9  != 0 :
    s = s + 9 - s % 9

e = e - e % 9
n = (e - s) // 9 + 1
sum = (s + e) * n // 2
print (sum)
