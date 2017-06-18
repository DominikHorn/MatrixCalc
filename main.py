from decimal import *
from matrix import Matrix
import copy

t = Matrix(3,3)
t[0] = 1, 1, 2
t[1] = 4, 0, 2
t[2] = 2, 1, 1
v = Matrix(3, 1)
v[0] = Decimal(4)/Decimal(3)
v[1] = 2
v[2] = - Decimal(2)/Decimal(3)

(c, l,r) = t.getLR()
print(c)
print(l)
print(r)
print(l*r)
