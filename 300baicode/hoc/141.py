input_list = list(map(int, input().split()))
check = False

for number_input_list in input_list :
    if number_input_list < 0 :
        print (f"{number_input_list}",end=" ")
        check = True
if not check :
    print("-")
