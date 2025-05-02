# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

x = int(input())
sizes = list(map(int, input().split(" ")))
n = int(input())
money_earned = 0
avail_sizes = Counter(sizes)

for _ in range(n):
    size, price = map(int, input().split(' '))
    if avail_sizes[size] > 0:
        money_earned += price
        avail_sizes[size] -= 1

print(money_earned)