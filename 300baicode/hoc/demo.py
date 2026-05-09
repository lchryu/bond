from collections import Counter


s = "aabbacbbb"

cnt = Counter(s)
print(cnt)
print(sorted(cnt))


T = ""
for i in sorted(cnt):
    T += i
print(T * 2)