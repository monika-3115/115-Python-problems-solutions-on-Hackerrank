# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = map(int, input().split(' '))
nl = list(map(int, input().split(" ")))
ma = set(map(int, input().split(' ')))
mb = set(map(int, input().split(' ')))
da = ma.difference(mb)
db = mb.difference(ma)
happy = 0
for i in nl:
    if i in da:
        happy+=1
    if i in db:
        happy-=1
print(happy)
