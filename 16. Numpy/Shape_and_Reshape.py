import numpy
n = list(map(int, input().split()))
l = numpy.array(n)
l.shape = (3,3)
print(l)
