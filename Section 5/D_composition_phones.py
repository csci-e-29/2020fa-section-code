# We want code to be *decoupled*, where classes/functions work independently and don't depend on one another


class Phone(object):
    my_phone = "samsung"


class CoolPhone(object):
    my_phone = "iphone 100"


class NewChild(object):  # Notice that we dont inherit anything this time around
    phone_type = Phone()  # this is the composition part -- I HAVE a phone, rather than "IS A" phone

    def override(self):
        print("I have a {} phone".format(self.phone_type.my_phone))  # now I'm calling an instance of the class


class CoolNewChild(object):
    phone_type = CoolPhone()

    def override(self):
        print("I have a much cooler {}".format(self.phone_type.my_phone))


NewChild().override()
CoolNewChild().override()
