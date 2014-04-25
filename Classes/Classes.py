class FirstClass(object):
    """description of class"""

    def setdata(self, value):
        self.data = value

    def getdata(self):
        return self.data


class SecondClass(FirstClass):
    def getdata(self):
        return 'Current value is ' + str(self.data)

class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value

    def __add__(self, other):
        return ThirdClass(self.data + other)

    def __mul__(self, other):
        return ThirdClass(self.data * other)

class NextClass:
    def printer(self, text):
        self.msg = text
        print(self.msg)