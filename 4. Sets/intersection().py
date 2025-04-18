# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
e = set(map(int, input().split()))
b= int(input())
f = set(map(int, input().split()))
ef = len(e)+len(f)-len(e|f)
print(ef)