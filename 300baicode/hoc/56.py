import math

def triangle_or_not (a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

def triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def triangle_perimeter(a, b, c):    
    return a + b + c


a , b , c ,= map(int, input().split())      

if triangle_or_not(a, b, c):

    x = triangle_area(a, b, c)
    y = triangle_perimeter(a, b, c)
    print('Day la 3 canh cua mot tam giac')
    print(f'{y:.2f} {x:.1f}')
else:
    print('Day khong phai la 3 canh cua mot tam giac')