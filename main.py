from decimal import *
from matrix import Matrix

t = Matrix(5,5)
x = Decimal(1)/Decimal(3)
t[0] = 0, .5, .5,  0,  0
t[1] = 1,  0,  0,  0,  0
t[2] = 0,  x,  0,  x,  x
t[3] = 0,  0,  0,  0,  1
t[4] = 0, .5, .5,  0,  0
print(t**1000)
