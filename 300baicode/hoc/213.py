# a = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
row, col = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(row)]
s = 0
for i in a:
     s += sum(i)
print(s)