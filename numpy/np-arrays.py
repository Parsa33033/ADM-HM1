import numpy

def arrays(arr):
    return numpy.flip(numpy.array(list(map(float, arr)), dtype=numpy.float))

arr = input().strip().split(' ')
result = arrays(arr)
print(result)