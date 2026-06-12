n = int(input())
x = int(input())
y = int(input())
ans = 0
for u in range(1, n + 1):
    for v in range(1, n + 1):
        if u == x and v == y:
            continue
        same_row = (u == x)
        same_col = (v == y)
        same_diag = (abs(u - x) == abs(v - y))
        if same_row or same_col or same_diag:
            if (u + v) % 2 == 0:
                ans += 1
print(ans)