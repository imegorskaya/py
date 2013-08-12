__author__ = 'wombat'
import math

class Solver:
    def demo(self):
        # q = b**2 - 4*a*c
        for i in range(10):
            a = int(input("a "))
            b = int(input("b "))
            c = int(input("c "))

            d = b ** 2 - 4 * a * c
            if d >= 0:
             disc = math.sqrt(d)
             root1 = (-b + disc) / (2 * a)
             root2 = (-b - disc) / (2 * a)
             print(root1, root2)
            else:
                print("error")


Solver().demo()

#def func():
#    if f is 0:
#    pass
#def func(self):
#    return x
#
#
#def func2(x):
#    y = func1(x.keys())
#    return y.startswith('foo')


