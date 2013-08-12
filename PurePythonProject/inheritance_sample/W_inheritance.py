__author__ = 'wombat'
__project__ = 'PurePythonProject'

class first(object):
    def first_check(self):
        print "First"

class second():
    def second_check(self):
        print "Second"

class third(first,second):
    def third_check(self):
        print "Third"


third().first_check()
