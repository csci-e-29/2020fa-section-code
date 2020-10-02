
'''
Exercises from:
 http://blog.thedigitalcatonline.com/blog/2014/08/20/python-3-oop-part-3-delegation-composition-and-inheritance/

Concepts:
  explicit delegation (composition)
  implicit delegation (inheritance)

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
        # add this: self.year = year

    @rv_decorator
    def add_ints(self, a, b):
        return a + b

        # Note: Calculator inherits divide_ints() implicitly

    # SmartWatch will not inherit but can be explicitly composed
    @rv_decorator
    def divide_ints(self, a, b):
        return a // b


class Calculator(Computer):
    # Calculator *is a* specific type of Computer

    speed = 'Slow'

    # TODO #1: if you run the program and type calc.__dict__ you get this:
    # > calc.__dict__
    #  {'computer_type': 'TI-84', 'speed': 'Fast'}

    # Fix the code so that the speed of the calculator is slow
    # also, make the year appear correctly in the dict by
    # adding self.year = year to the Computer init function

    '''                          
    Solution #1:                                                            
    def __init__(self, computer_type='Calculator', year=1970):
      super().__init__()
      self.computer_type = computer_type
    '''

    # TODO #2: Override add_ints to create a version that takes 3 seconds longer to run (calc is slower than comp)
    # but reuse the logic from the parent class (that is, call the parent's function, don't rewrite `return a+b`)

    # Solution #2 :
    '''
    @rv_decorator
    def add_ints(self, a, b):
      time.sleep(3)
      return super().add_ints(a,b)
    '''


# TODO #3: write a class called Smartwatch that uses the add_inits method from Calculator
# using composition instead of inheritance. Discuss the benefits/drawbacks of both patterns

'''
Solution #3
class SmartWatch():
  def __init__(self, computer_type='Watch', year=2015):
    self._calc = Calculator('Apple Watch', 2019)

  @rv_decorator
  def  add_ints(self, a, b):
    print('SmartWatch class')
    return self._calc.add_ints(a,b)
'''

calc = Calculator('TI-84', 2012)
watch = SmartWatch('Samsung')