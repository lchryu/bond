n = int(input())
a = 0
from tqdm import tqdm
for i in tqdm(range(15, n + 1, 15), desc="Dang tinh toan"):
    a = a + i
    print(i)
print(a)