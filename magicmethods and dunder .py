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


class Practical:
    def __init__(self, name):
        self.name = name

class Person(Practical):
    def __init__(self, names):
        super().__init__(names)

obj = Practical(['Chemistry', 'Physics', 'Computer'])
for subject in obj.name:
    print(subject)
print(obj.name)

obj1 = Person(["Nafees", "Hasnat", "Zohaib", "Farhan", "Umair"])
for name in obj1.name:
    print(name)
print(obj1.name)

# __init__:
# Create a class representing a book. Implement the __init__ method to initialize attributes such as title, author, and pages.

class Book:
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages

BOOK1=Book(
    "The Hitchhiker's Guide to the Galaxy",
    "Douglas Adams", 
    215
)
        
print(BOOK1.title)
print(BOOK1.author)
print(BOOK1.pages)