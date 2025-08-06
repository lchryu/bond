def perfect (n) :
    add = 0
    for i in range (1 , n ) :
        if n % i == 0  :
            add += i
    if add == n :
        return "Yes"
    return 'No' 
n = int(input())
print(perfect (n))
