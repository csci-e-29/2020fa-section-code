# Using @property decorator
class USCurrency:
    def __init__(self, value=0):
        self._value = value

    def to_new_currency(self, rate, to="NCR"):
        rate = rate if rate > 0 else 1
        return self._value * rate

    @property
    def curr_value(self):
        print("Getting value...")
        return self._value

    @curr_value.setter
    def curr_value(self, value):
        print("Setting value...")
        self._value = value


# create an object
money = USCurrency(37)
print(money.curr_value)
print(money.to_new_currency(1.1, "GBP"))

