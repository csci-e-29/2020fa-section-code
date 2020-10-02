class DescriptorClass:
    def __set__(self, instance, value):
        print("setting hello!", "- 6th print statement")
        instance.__dict__["_hello"] = value + 1
    def __get__(self, instance, val):
        return instance.__dict__["_hello"]


class FakeClass:
    def meh(self):
        print("I'm actually in meh now!", "- 1st print statement")
        return "meh"


class ExampleClass:
    class_var = FakeClass().meh()  # Here you'll see it prints "I'm actually in meh now!" -- this is where it gets assigned!
    class_var_2 = DescriptorClass()  # But here nothing is getting assigned yet. It's getting delayed until you call __set__ in the instance.

    def __init__(self, param):
        print(self.__dict__, "- 3rd print statement")  # self's dict is empty because we haven't set any instance attributes yet!
        print(self.class_var, "- 4th print statement")  # but I can still access class level attributes!
        self.class_var = "bleh!"
        print(self.__dict__, "- 5th print statement")  # and if I check self's dict now, we can see "class_var" in the instance dict. Note that method meh is not being called!
        self.class_var_2 = param  # now we're calling the descriptor's set.
        # self.class_var_2 = 100  # if you run this, the print statement will actually get called again!


print(ExampleClass.class_var, "- 2nd print statement")  # this works as it is a class attribute
t = ExampleClass(12)
print(t.class_var_2, "I called get")
