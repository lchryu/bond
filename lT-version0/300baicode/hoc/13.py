a = int (input ())

x = a % 10  # 4
# a = a // 10 # 123
y = (a % 100) // 10
z = (a % 1000) // 100
t = a // 1000

print(x + y + z + t)