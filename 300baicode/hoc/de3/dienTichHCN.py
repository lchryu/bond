a = int(input())
b = int(input())
c = int(input())
areaA_B = a* b
areaB_C = c*b
areaC_A = a*c
print(max(areaA_B, areaB_C, areaC_A))