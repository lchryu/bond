def dem_so_uoc (a) :
    cnt = 0 
    for i in range (1 ,a + 1  ) :
        if a % i == 0 :
            cnt += 1
    return cnt
if __name__=="__main__":
    a = int(input())
    print(dem_so_uoc(a))