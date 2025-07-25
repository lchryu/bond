n = int(input())

rev = 0

# n = 0
# rev = 321

while n != 0:
    rev = rev * 10 + n % 10
    n //= 10

print(rev)    
