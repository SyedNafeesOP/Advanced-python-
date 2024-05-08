# In Python, "magic methods" are special methods with double underscores (also called "dunder" methods, short for "double underscore"). These methods allow you to define how objects of your class behave in certain situations. They are called "magic" because they are invoked automatically behind the scenes in response to certain operations on objects.

class Mobile:
    def __init__(self,name,Ram,Processor):
        self.name=name
        self.Ram=Ram
        self.Processor=Processor
M1=Mobile("Samsung galaxy a15",8,"Octa-core Dimensity 720")   
print(M1.name)
print(M1.Ram)
print(M1.Processor)

class Numbers:
    def __init__(self, numbers, number):
        self.numbers = numbers
        self.number = number

    def __add__(self):
        return self.numbers + self.number

N1 = (5, 6)
n = Numbers(N1, 0)
print(n.__add__())  # output: 1