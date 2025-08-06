def tong (m) :
    s = 0 
    for i in range (1 , m+ 1) :
        s += i
    return s

def tnonchecker (n) :
    m = 0
    while tong(m) < n :   
        m += 1
    return tong(m) == n
def main () :
    a = int(input())
    if tnonchecker(a):
        print("Yes")
    else: print("No")

main()


