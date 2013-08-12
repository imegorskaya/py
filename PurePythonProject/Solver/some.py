__author__ = 'mio'
__project__ = 'PurePythonProject'
s = "foo{0}".format("bar")
print( s)
s1= "foo%s" % "bar"
print(s1)
s2 = "foo" + "bar"
print (s2)
class Some:
    def method_name(self):
        return "Hello, World!"

    def print_hello(self):
        s = self.method_name()
        print(s)

