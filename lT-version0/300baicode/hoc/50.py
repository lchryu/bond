a = float(input())

if a <= 50 :
    print ( a * 600)
elif a <= 100 :
    print(50 * 600 + (a - 50)* 800)
elif a <= 200:
    print (50 * 600 + 50 * 800 + (a - 100)* 1100)
else :
    print (50 * 600 + 50 * 800 + 100 * 1100 + (a - 200)* 1500)