
__author__ = 'wombat'
__project__ = 'PurePythonProject'
# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    """

    :param n:
    """
    c, b = 0, 1
    while b < n:
        print b,
        c, b = b, c+b


def fib2(n): # return Fibonacci series up to n
    result = []
    c, b = 0, 1
    while b < n:
        result.append(b)
        c, b = b, c+b
    return result

