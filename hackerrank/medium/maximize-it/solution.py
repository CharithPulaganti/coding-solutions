from itertools import product

K, M = map(int, input().split())

lists = []

for _ in range(K):
    values = list(map(int, input().split()))
    lists.append(values[1:])
    
maximum = 0

for combination in product(*lists):
    value = sum(x **2 for x in combination) % M
    maximum = max(maximum, value)
    
print(maximum)
