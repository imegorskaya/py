from pydoc import text


def f(a, **kwargs):
    """Renders a template from the given template source string with the given context.

    :param a: normal parameter
    :param b: unresolved parameter false positive
    """
    pass

f(1)

def myLondNameMethod():
    pass

def fibonacci(n, a=0, b=1):
    while b < n:
        print( b )
        a, b = b, a+b
# Now call the function we just defined...
n = input("n = ")

fibonacci(n,0,1)

input( '\n\nPress Enter to exit...' )



