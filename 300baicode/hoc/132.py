a = int(input())

hahaha = [int(input()) for i in range(a)]
new_list_hahaha = [i for i in hahaha if i % 2 == 0]
if len(new_list_hahaha) != 0 :
    print(f"{sum(new_list_hahaha)/len(new_list_hahaha):.3f}")
else :
    print("0.000")    