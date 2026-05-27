s = input()

best = "0"

for d in "0123456789":
    for x in "0123456789":
        t = ""

        for c in s:
            if c == d:
                t += x
            else:
                t += c

        # không có số 0 ở đầu
        if t[0] == '0':
            continue

        # kiểm tra chia hết cho 9
        if sum(int(c) for c in t) % 9 != 0:
            continue

        # lấy max
        if len(t) > len(best) or (len(t) == len(best) and t > best):
            best = t

print(best)