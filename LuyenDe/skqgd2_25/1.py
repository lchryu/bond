A = int(input())
B = int(input())
m = max(A,B)
n = min(A, B)
mn = m - n

if m == B :
    mn += 5
else:
    mn = abs(5 - mn)
print(mn)    
    