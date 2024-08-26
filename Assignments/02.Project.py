import math

a = float(input("Enter Side 1: "))
b = float(input("Enter Side 2: "))
c = float(input("Enter Side 3: "))

#s = semiperimeter
s = float((a + b + c) / 2)

from math import sqrt
sa = s - a
sb = s - b
sc = s - c
ss = s * sa * sb * sc
area = sqrt(ss)
print("Area:", area)