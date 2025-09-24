n = int(input())
a = []
for i in range (n) :
    y = int(input())
    a.append (y)

new_a = [a[i] for i in range (n) if a[i]  % 5 == 0]
print(len(new_a))