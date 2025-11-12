user_input = list(map(int, input().split()))
x, k = map(int, input().split())
user_input.insert(k, x)
for x in user_input :
    print(x)