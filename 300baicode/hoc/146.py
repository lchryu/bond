a = list(map(int , input().split()))
def my_sorting (a):
    b = []
    for i in range (len(a)):    
        b.append(max(a))
        a.remove(max(a))
    b.reverse()
    return b
print(*my_sorting(a))        