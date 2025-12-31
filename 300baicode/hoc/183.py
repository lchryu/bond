str_input = input()
for x in str_input:
    if x.isdigit() or x.isalpha()  :
        print("NO")
        break
else:
    print("YES")

