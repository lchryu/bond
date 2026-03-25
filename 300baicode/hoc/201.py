num_input = int(input())
x = []
for i in range(num_input):
    x.append(input())
for b in x :
    if b == "":
        print(" ", end="")
    else: print(b, end= "")

