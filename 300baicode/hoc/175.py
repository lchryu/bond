a = input()
if a == "z":
    print("a")
elif a == "Z":
    print("A")
else:
    a_index = ord(a)
    b = chr(a_index + 1)
    print(b)

