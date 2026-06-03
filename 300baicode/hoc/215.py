a = int(input())
b = [input() for _ in range(a)]
c = [float(input()) for _ in range(a)]
for name, score in zip(b, c):
    print(f"{name}: {score:.1f}")
