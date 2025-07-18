def howmanyeven (a , b) :
    cnt = 0 
    for i in range (a , b + 1) :
        if i % 2 == 0 :
            cnt += 1
    return cnt        

if __name__ == "__main__":
    a , b = map(int, input().split())
    print(howmanyeven(a, b))