string_input = input()
string_input2 = input()
num_input = int(input())
output_string =  string_input[:num_input] + string_input2 + string_input[num_input:]
print(output_string)