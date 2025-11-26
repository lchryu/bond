def is_num_under_0(x) :
    if x > 0 :
        return False
    return True
check = False
user_input = list(map(int, input().split()))
for x in user_input:
    if is_num_under_0(x) :
        check = True
        break
    else :
        check = False
if check :
    print("YES")
else:
    print("NO")
