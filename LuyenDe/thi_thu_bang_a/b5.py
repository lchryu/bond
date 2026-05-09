a = input()
n = len(a)
ans = 0
for c in "abcd":
    t = 0
    for i in a:
        if i == "0" or i == c :
            t += 1
            ans = max(ans, t)
        else: t = 0
print (min(ans, n))        
