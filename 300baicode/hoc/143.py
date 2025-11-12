input_list = list(map(int, input().split()))
cnt  = 0
for number_input_list in input_list :
    if number_input_list < 0 :
        cnt += number_input_list
print(cnt)        