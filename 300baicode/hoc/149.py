user_input = list(map(int, input().split()))
k = int(input())
user_input.pop(k)
for x in user_input :
    print(x)
