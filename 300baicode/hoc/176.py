a = input()
if a == "a":
    print("z")
elif a == "A":
    print("Z")
else:
    a_index = ord(a)
    b = chr(a_index - 1)
    print(b)

