class Dog():
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def bark(self):
        print(f'{self.name} says woof!')

    def __str__(self):
        return f'The dog named {self.name} is {self.age} years old.'

print(Dog('Ruby', 4))