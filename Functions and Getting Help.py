#Order of operations
#The arithmetic we learned in primary school has conventions about the order in which operations are evaluated. 
#Some remember these by a mnemonic such as PEMDAS - Parentheses, Exponents, Multiplication/Division, Addition/Subtraction.


#a, b = b, a#swapping

#help(round)
#help(round(-2.01))
#help(print)

def least_difference(a, b, c):
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)

help(least_difference)
#Python isn't smart enough to read my code and turn it into a nice English description. 
#However, when I write a function, I can provide a description in what's called the docstring.
#docstring
def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c.
    
    >>> least_difference(1, 5, -5)
    4
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)
help(least_difference)

Functions that don't return¶
What would happen if we didn't include the return keyword in our function?


def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c.
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    min(diff1, diff2, diff3)
    
print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7),
)
#result None None None

help(print)
'''
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
'''
print(1, 2, 3, sep=' < ') #1 < 2 < 3


#optional arguments with default values to the functions
def greet(who="Colin"):
    print("Hello,", who)
    
greet()#Hello, Colin
greet(who="Kaggle")#Hello, Kaggle
# (In this case, we don't need to specify the name of the argument, because it's unambiguous.)
greet("world")#Hello, world


def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)

def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))

print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1), 
    sep='\n', # '\n' is the newline character - it starts a new line
)













