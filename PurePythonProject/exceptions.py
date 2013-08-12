__author__ = 'mio'
__project__ = 'PurePythonProject'
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
except ValueError:
    print "Could not convert data to an integer."
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise

class MyError(Exception):
    def __init__(self, value):
            self.value = value
    def __str__(self):
         return repr(self.value)
try:
     raise MyError(2*2)
except MyError as e:
    print 'My exception occurred, value:', e.value