def is_above_0 (a) :
    if a > 0 :
        return True
    else : return False
user_input = list(map(int, input().split()))
check = True
for x in user_input:
    if is_above_0(x) :
        pass
    else :
        check = False
if check :
    print("YES")
else:
    print("NO")