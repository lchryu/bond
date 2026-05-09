a = int(input())
b = int(input())
c = int(input())
a_b = a + b
b_c = b + c 
a_c = a + c
d = []
if a_b % 2 == 0 :
    d.append(a_b)
if b_c % 2 == 0 :
    d. append (b_c)
if a_c % 2 == 0 :
    d. append (a_c)
print(max (d))            


