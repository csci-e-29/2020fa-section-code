'''
Exercises from:
 http://blog.thedigitalcatonline.com/blog/2014/08/20/python-3-oop-part-3-delegation-composition-and-inheritance/

Concepts:
  implicit delegation (inheritance)
  explicit delegation (composition)

'''
import time
from functools import wraps


def rv_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwds):
        rv = func(*args, **kwds)
        print("name of function: " + func.__name__)
        print("return value" + str(rv))
        return rv

    return wrapper


class Computer:
    # Computer is a general purpose computing device

    def __init__(self, computer_type='General Purpose Compute', year=1995):
        self.computer_type = computer_type
        self.speed = 'Fast'

    @rv_decorator
    def add_ints(self, a, b):
        return a + b

    @rv_decorator
    def divide_ints(self, a, b):
        return a // b


class Calculator(Computer):
    # Calculator *is a* specific type of Computer

    speed = 'Slow'

    # TODO: Override add_ints to create a version that takes 3 seconds longer to run (calc is slower than comp)
    # but reuse the logic from the parent class (that is, call the parent's function, don't rewrite `return a+b`)
    @rv_decorator
    def add_ints(self, a, b):
        time.sleep(3)
        pass


# TODO: write a class called Smartwatch that uses the add_inits method from Calculator
# Using composition instead of inheritance. Discuss the benefits/drawbacks of both patterns

'''
class SmartWatch():
...
'''

calc = Calculator('TI-84', 2012)

