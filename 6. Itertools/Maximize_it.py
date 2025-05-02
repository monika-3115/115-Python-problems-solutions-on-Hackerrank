# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

k,m = map(int, input().split(' '))
lists = []
max_sum = 0
for _ in range(k):
    n = list(map(int, input().split(' ')))
    lists.append(n[1:])
for c in product(*lists):
    curr_sum = sum(x**2 for x in c) % m
    max_sum = max(max_sum, curr_sum)
print(max_sum)