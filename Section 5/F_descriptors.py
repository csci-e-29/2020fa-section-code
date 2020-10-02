# From Fluent Python by Buciano Ramalho


class LineItem:  # Imagine we want to implement a class that tracks items at a grocery store
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def subtotal(self):
        return self.weight * self.price


item = LineItem("apple", 2.9, 2.1)
item.price = -0.9  # reset the attribute price for the item instance
setattr(item, "weight", -0.8)  # equivalent to item.weight = -0.8


# print(item.subtotal())

# Let's revisit but with descriptor instead


class Quantity:
    def __init__(self, label_name):
        self.label_name = "_" + label_name  # this label is a private variable otherwise ends up repeatedly invoking __set__

    def __set__(self, instance, value):
        # What is instance? Here it's the instance of LineItem that we created
        if value < 0:
            raise ValueError("Invalid entry, can't be less than 0. You entered {}".format(value))

        instance.__dict__[
            self.label_name] = value  # in the instance, add to it's __dict__ (object's namespace) {self.label_name, value}

    def __get__(self, instance, random):
        return instance.__dict__[self.label_name]


class LineItem:
    weight = Quantity(
        "weight")  # Because this is a class attr that implements the descriptor protocol, python steps in and invokes __get__ or __set__ rather than setting/getting the attribute
    price = Quantity("price")

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight  # this is not an attribute, it's a descriptor on the class and access via the descriptor protocol
        self.price = price

    def subtotal(self):
        return self._weight * self._price  # here remember it's a private variable, i.e. accessed with __ in front


truffle = LineItem("white truffle", 20, 500)


# print(truffle.price)  # this will invoke the __get__ from the descriptor protocol
# print(LineItem.__dict__)
# print(truffle.subtotal())


class Verbose_attribute():
    def __get__(self, obj, type=None) -> object:
        print("accessing the attribute to get the value")

        return self

    def __set__(self, obj, value) -> None:
        print("accessing the attribute to set the value")
        raise AttributeError("Cannot change the value")


class Foo():
    attribute1 = Verbose_attribute()
    # print(attribute1.__class__.__mro__)

my_foo_object = Foo()
print(my_foo_object.attribute1)
# my_foo_object.attribute1 = 32
# print(my_foo_object.attribute1)
