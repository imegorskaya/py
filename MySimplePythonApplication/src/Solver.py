import math


class Solver:

    a=1
    b=2
    c=3
    def calculate(self,a,b,c):


        d = b ** 2 - 4 * a * c
        if d>=0:
            disc = math.sqrt(d)
        else:
            print ("error")
        root1 = (-b + disc) / (2 * a)
        root2 = (-b - disc) / (2 * a)
        print(root1, root2)

class MyPythonFile():
    def doSmth(self):
        pass

Solver().calculate(6,2,4)