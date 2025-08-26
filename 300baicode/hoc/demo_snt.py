from math import isqrt
def snt_optimize(n: int):
    if n < 2:
        return False
    dem_toi_uu = 0
    for i in range(2, isqrt(n) + 1):
        dem_toi_uu += 1
        if n % i == 0:
            return False
    return dem_toi_uu

def snt(n: int):
    if n < 2:
        return False
    dem = 0
    for i in range(2, n + 1):
        dem += 1
        if n % i == 0:
            return False
    return dem

n = 100003
dem_optimize =  snt_optimize(n)  # Example usage
dem = snt(n)

print(dem_optimize, dem)