list_input  = list(map(int, input().split()))
new_list =  list(filter(lambda num_in_li : num_in_li % 2 == 0 , list_input))
# if len(new_list) == 0 :
#     print("-")
# else:
print(*new_list, sep='\n')
