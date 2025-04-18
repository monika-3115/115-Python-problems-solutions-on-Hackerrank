# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
for _ in range(t):
    a = int(input())
    sa = set(map(int, input().split()))
    b = int(input())
    sb = set(map(int, input().split()))
    print(sa.issubset(sb))
