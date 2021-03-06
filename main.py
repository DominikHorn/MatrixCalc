from decimal import *
from matrix import Matrix
import copy

matrnr = 12345678
x7 = Decimal(int((matrnr / 1) % 10))
x6 = Decimal(int((matrnr / 10) % 10))
x5 = Decimal(int((matrnr / 100) % 10))
x4 = Decimal(int((matrnr / 1000) % 10))
x3 = Decimal(int((matrnr / 10000) % 10))
x2 = Decimal(int((matrnr / 100000) % 10))
x1 = Decimal(int((matrnr / 1000000) % 10))

t = Matrix(14,14)
t[0]  = 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, x7
t[1]  = 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, x6, 0
t[2]  = 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, x5, 0, 0
t[3]  = 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, x4, 0, 0, 0
t[4]  = 0, 0, 0, 0, 10, 0, 0, 0, 0, x3, 0, 0, 0, 0
t[5]  = 0, 0, 0, 0, 0, 10, 0, 0, x2, 0, 0, 0, 0, 0
t[6]  = 0, 0, 0, 0, 0, 0, 10, x1, 0, 0, 0, 0, 0, 0
t[7]  = 0, 0, 0, 0, 0, 0, x7, 10, 0, 0, 0, 0, 0, 0
t[8]  = 0, 0, 0, 0, 0, x6, 0, 0, 10, 0, 0, 0, 0, 0
t[9]  = 0, 0, 0, 0, x5, 0, 0, 0, 0, 10, 0, 0, 0, 0
t[10] = 0, 0, 0, x4, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0
t[11] = 0, 0, x3, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0
t[12] = 0, x2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0
t[13] = x1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10
(c, l, r, p) = t.getLR()
print(c)
print(l)
print(r)
print(p)
print(l*r)
print(p*t)
print(p * t == l * r)
