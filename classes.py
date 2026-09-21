#Python	Runs when	JavaScript equivalent
#__init__	You create an object, like Dog('Ruby', 4)	constructor
#__str__	You print() the object or call str() on it	toString()
#self	Always the first parameter; the object itself	this
class Dog():
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def bark(self):
        print(f'{self.name} says woof!')

    def __str__(self):
        return f'The dog named {self.name} is {self.age} years old.'

print(Dog('Ruby', 4))
