from math import *
def cnt (a , b) :
    cnnt = 0 
    for i in range (a , b + 1) :
        if i % 5 == 0  :
            cnnt += 1
    return cnnt

def dvisable (a , b) :
    total = []
    for i in range (a , b + 1) :
        if i % 5 == 0 :
            total.append(i)
    return total

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(cnt(a, b), *dvisable(a, b), sep=' - ')