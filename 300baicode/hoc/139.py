a = int(input())
b = [int(input())for i in range (a)]

def is_prime (a) :
    if a <= 1 : 
        return False
    for i in range (2 ,int( (a**0.5) + 1)) :
        if a % i == 0 :return False
    return True
cnt = 0
total = 0
for index in b :
    if is_prime (index) :
        total += index
        cnt += 1
if total == 0 :
    print("0.0")
else:
    print(f"{total / cnt :.1f}")        