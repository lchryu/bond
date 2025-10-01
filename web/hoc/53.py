d = int(input())

if d < 18 :
    print('Tre em')
    if d <= 6 :
        print('Tre mam non')
    elif d <= 11 :
        print('Tre tieu hoc')
    else :
        print('Tre trung hoc')
elif d < 60 :
    print('Nguoi truong thanh')
    if d <= 23:
        print('Sinh vien')
    else :
        print('Nguoi di lam')
else :
    print('Nguoi cao tuoi')
    if d <= 62 :
        print('Sap nghi huu')
    else :
        print('Da nghi huu')