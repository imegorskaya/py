__author__ = 'wombat'
import math

class SimpleEquation:
    def demo(self, a, b, c):
        d = math.sqrt(b ** 2 - 4 * a * c)
        root1 = (-b + d) / (2 * a)
        root2 = (-b - d) / (2 * a)
        print(root1, root2)


SimpleEquation().demo(3,2,1)
