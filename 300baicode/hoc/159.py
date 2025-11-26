list_input = list(map(int, input().split()))
check = False
for index , num in enumerate(list_input) :
    if num % 2 == 0 :
        check = True
        print(index, num)
if not check :
    print("-")