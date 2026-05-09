a = int(input())
b = int(input())
c = int(input())
sum_a_b = a + b
du = c % sum_a_b
so_lan = c // sum_a_b
so_bi_do = a * so_lan
if du > a :
    so_bi_do += a
if du <= a :
    so_bi_do += du
print(so_bi_do)       

