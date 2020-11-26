import enum

class QuantityMeasurements:
    def __init__(self, unit, value):
        '''
         declared __init__ constructor to initialize the
         attributes of Class QuantityMeasurements

        :param unit: unit will be provided by user
        :param value: value will be provided by user
        '''
        self.unit = unit
        self.value = value

    def __eq__(self, another):
        '''

        :param another: it will be provided by user itself
        :return:
        '''
        if isinstance(another, QuantityMeasurements):
            return self.value == another.value
        return False

    def compare(self, another):
        '''

        :param another:it will be provided by user itself
        :return: it returns whether true or false
                 if both the units before and after conversion  are equal
                 it ruturns true otherwise returns false
        '''
        if self.unit.__class__ == another.unit.__class__:
            if self.unit.__class__.convert(self.unit, self.value) == another.unit.__class__.convert(another.unit,
                                                                                                          another.value):
                return True
        return False

    def add(self, another):
        '''

        :param another: it will be provide by user
        :return: it returns the addition of both the values
                    after conversion
        '''
        if self.unit.__class__ == another.unit.__class__:
            return self.unit.__class__.convert(self.unit, self.value) + another.unit.__class__.convert(
                another.unit, another.value)
        return 0


class Weights(enum.Enum):
    kilo_gram = 1.0
    gram = 0.001
    milligram = 0.000001
    tonne = 1000

    def __init__(self, unit):
        self.unit = unit

    def convert(self, value):
        return self.unit * value

class Distance(enum.Enum):
    feet = 12
    inch = 1.0
    yard = 36.0
    cm = 0.4
    meter = 39.4

    def __init__(self, unit):
        self.unit = unit

    def convert(self, value):
        return self.unit * value

class Temperature(enum.Enum):
    celsius = 1.8
    fahrenheit = 1

    def __init__(self, unit):
        self.unit = unit

    def convert(self, value):
        if self == Temperature.celsius:
            return self.unit * value + 32
        else:
            return self.unit * value