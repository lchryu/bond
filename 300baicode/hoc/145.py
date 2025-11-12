input_list = list(map(int, input().split()))
smallest_negative = 1
blablablablablableblablablu = None

for i in range(len(input_list)) :
    if input_list[i] < 0 and input_list[i] < smallest_negative :
        smallest_negative = input_list[i]
        blablablablablableblablablu = i
if not blablablablablableblablablu == None : 
    print(smallest_negative)
    print(blablablablablableblablablu)
else:
    print("-")    

