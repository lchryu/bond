d = int(input())

if d >= 80 :
    print('Loai A')
    if d >= 90 :
        print('Xuat sac')
    else :
        print('Gioi')
elif d >= 50 :
    print('Loai B')
    if d >= 65:
        print('Kha')
    else :
        print('Trung binh')
else :
    print('Loai C')
    if d >= 35 :
        print('Yeu')
    else :
        print('Kem')