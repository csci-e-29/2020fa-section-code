# From Learn Web Development with Python by Fabrizio Romano

# Using inheritance often leads to multiple inheritance problems, known as "diamond inheritance"


class A:
    def print_name(self):
      print("a")


class B(A):
    def print_name(self):
      print("b")


class C(A):
    def print_name(self):
      print("c")


class D(B, C):

    pass


d = D()
d.print_name()  # label could almost be either c or b!

"""
This order is called linearization of class D, and the set of rules applied are called MRO (Method Resolution Order). 
"""

# To get the MRO of a class, you can use either the __mro__ attribute or the mro() method.
print(d.__class__.__mro__)  # MRO = method resolution order