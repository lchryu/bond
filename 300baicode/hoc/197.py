s = input()
n = int(input()) - len(s)
result = s.zfill(len(s) + n)   # thêm n số 0 bên trái
print(result)  # 00000123