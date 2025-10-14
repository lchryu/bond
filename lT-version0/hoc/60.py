def tach_chu_so(n: int) -> list:
    chu_so = []
    while n > 0:
        chu_so.append(n % 10)
        n = n // 10
    return chu_so


# print(max(tach_chu_so(123456)))

def max_digit(n: int) -> int:
    gtln: int = -1

    while n > 0:
        r: int = n % 10
        n //= 10
        
        if r > gtln:
            gtln = r

    return gtln
if __name__ == "__main__" :
    a = int(input())
    arr = tach_chu_so(a)

    gtln = -1
    for x in arr:
        if x > gtln:
            gtln = x
    print(gtln)


    gtnn = 10
    for i in arr :
        if i <  gtnn :
            gtnn = i 
    print(gtnn)
