a = int(input())
b = [int(input()) for i in range (a)]
index_out = float('-inf')
container = float('-inf')
for index in range (a) :
    if b[index] > container :
        index_out = index
        container = b[index]
print(container , end = " " )
print(index_out)

# -1  -2 -5