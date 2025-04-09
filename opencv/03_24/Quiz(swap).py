def swap(a, b):
    return b, a


a = 1
b = 2
print('swap 전:', a, b)
a, b = swap(a, b)
print('swap 후:', a, b)