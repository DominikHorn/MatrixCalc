from decimal import *
from matrix import Matrix
import copy

sg = Matrix(6,5)
sg[0] = 1, 1, 0, 0, 0
sg[1] = 0, 1, 1, 0, 0
sg[2] = 0, 0, 1, 0, 0
sg[3] = 1, 0, 0, 1, 1
sg[4] = 0, 0, 0, 1, 0
sg[5] = 0, 0, 0, 0, 1
a = Matrix(5,5)
for i in range(5):
    a[i] = sg[i]
b = Matrix(5,5)
b[0] =  1, -1,  1,  0,  0
b[1] =  0,  1, -1,  0,  0
b[2] =  0,  0,  1,  0,  0
b[3] =  0,  0,  0,  0,  1
b[4] = -1,  1, -1,  1, -1

x1 = b.columnAt(0)
x2 = b.columnAt(1)
x3 = b.columnAt(2)
x4 = b.columnAt(3)
x5 = b.columnAt(4)

print("x1: " + str(sg*x1))
print("x2: " + str(sg*x2))
print("x3: " + str(sg*x3))
print("x4: " + str(sg*x4))
print("x5: " + str(sg*x5))
