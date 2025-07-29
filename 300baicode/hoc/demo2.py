import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


n = int(input())
gtln = -1
while n != 0:
    r = n % 10
    n //= 10
    
    if r > gtln:
        gtln = r 
        
print(gtln)
    
    