import numpy
n,m = map(int, input().split())
l = []
for _ in range(n):
    m = input().strip().split()
    l.append(m)
    ln = numpy.array(l)
ln = ln.astype(int)
print(numpy.transpose(ln))
print(ln.flatten())
