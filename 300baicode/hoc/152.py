user_input = list(map(int, input().split()))
user_input_2 = list(map(int, input().split()))
user_input.extend(user_input_2)
print(*user_input)