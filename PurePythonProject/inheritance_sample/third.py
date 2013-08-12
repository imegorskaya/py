from inheritance_sample.first import first
from inheritance_sample.second import second

__author__ = 'wombat'
__project__ = 'PurePythonProject'

class third(first,second):
    def third_check(self):
        print "Third"


third().first_check()
 