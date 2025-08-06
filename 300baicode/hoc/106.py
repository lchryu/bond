def prime_or_not(n) :
    if n <= 1:
        return "No"
    for i in range (2 , n ) :
        if n % i == 0 :
            return "No"
    return "Yes"
if __name__=="__main__" :
    n = int(input())
    print(prime_or_not(n))
