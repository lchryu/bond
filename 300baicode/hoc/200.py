text = input()
i = int(input())
b = input()
text = list(text)
text[i] = b
print(*text, sep='')