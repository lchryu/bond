def SOL(k):
    i = 0
    cnt = 0
    while True :
        if i % 2 == 0 :
          print(i , end = " ")
          cnt+= 1
        i += 1
        if cnt == k :
            break 
if __name__ == "__main__" :              
    SOL(int(input()))