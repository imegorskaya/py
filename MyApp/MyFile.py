__author__ = 'mio'
__project__ = 'MyApp'
import math
a = int(input("a "))
b = int(input("b "))
c = int(input("c "))

d = b ** 2 - 4 * a * c
if d >= 0:
    disc = math.sqrt(d)
    root1 = (-b + disc) / (2 * a)
    root2 = (-b - disc) / (2 * a)
    print(root1, root2)