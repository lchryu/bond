input_list = list(map(int, input().split()))
cnt  = 0
sum = 0
for number_input_list in input_list:
    if number_input_list < 0:
        sum += number_input_list
        cnt += 1
if cnt != 0:
    avg = sum / cnt
    print(f"{avg :.1f}")
else: print("0.0")