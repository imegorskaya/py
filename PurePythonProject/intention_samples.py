__author__ = 'mio'
__project__ = 'PurePythonProject'
def g(x):
    return x

def f(x):
    y = g(x.keys())
    return y.startswith('foo')

