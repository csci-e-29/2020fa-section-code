# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    # Inheritance
    # composition
    # property
    # used as a decorator
    # descriptors

    # Examples from "Learn Python 3 the Hard Way" by Zed A Shaw

    class Parent(object):
        def __init__(self):
            self.phone_type = "iphone"
            # self.mood = "happy" # if I change this attribute here, it won't get inherited!

        def implicit(self):
            print("I am a person!")

        def override(self):
            print("I have an {}".format(self.phone_type))

        def altered(self):
            self.mood = "happy"
            print("Time to hug child!")


    class Child(Parent):  # Child will inherit from Parent
        def __init__(self):
            self.phone_type = "samsung"
            self.mood = "sad"

        def override(self):
            print("Override in Child")
            print("I have an {}".format(self.phone_type))

        def altered(self):
            print("My current mood is {}".format(self.mood))
            super().altered()
            print("And now my mood is {}".format(self.mood))


    parent = Parent()
    child = Child()

    parent.implicit()
    child.implicit()  # we'll inherit directly from the Parent class

    parent.override()
    child.override()  # we override the parent class. We want the functionality of this class to behave differently

    child.altered()  # note that when I call super I can change the attributes in the child class!

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

'''
feedback from arman:
 - more training would be good
 - 
'''
