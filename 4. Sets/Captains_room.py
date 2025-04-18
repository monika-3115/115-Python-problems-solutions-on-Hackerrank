# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())
r = list(map(int, input().split()))
c = (k * sum(set(r)) - sum(r)) // (k-1)
print(c)
