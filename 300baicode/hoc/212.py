n = int(input())
names = [input() for _ in range(n)]
names.sort(key=lambda x:(x.split()[-1], x[:len(x)]))
print(*names, sep='\n')