def rectangle_or_not(a, b,):
    if a <= 0 or b <= 0:
        return False
    return True

def rectangle_area(a, b):
    return a * b

def rectangle_perimeter(a, b):
    return 2 * (a + b)
a, b = map(int, input().split())

if rectangle_or_not(a, b):
    area = rectangle_area(a, b)
    perimeter = rectangle_perimeter(a, b)
    print('Day la 2 kich thuoc cua mot hinh chu nhat')
    print(f'{perimeter} {area}')

else:
    print('Day khong phai la 2 kich thuoc cua mot hinh chu nhat')

    if a < 0 and b < 0:
        print('a va b la so am')
    else:
        if a < 0 :
            print('a la so am')
        if b < 0:
            print('b la so am')
