a = int(input())
n = list(map(int , input().split()))
output = (n [i] for i in range (a) if n[i] % 3 == 0)
print(sum(output))
       