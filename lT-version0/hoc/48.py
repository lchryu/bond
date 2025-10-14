a , b , c = map(int,input().split())


if a + b > c and b + c > a and c + a > b :
    print ('Yes')
    if a == c and a == b and c == b :
        print ('Deu')
    elif a == c or a == b or b == c :
        print('Can')
    elif a * a + b * b  == c*c or a *a + c * c == b or b *b + c*c ==a * a :
        print("Vuong")
    else :
        print('Thuong')
else :
    print ('No')    