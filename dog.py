# dog.py
class Dog:
  def __init__(self, name, breed):
    self.name = name
    self.breed = breed
    print("dog initialized!")

  def bark(self):
    print("Woof!")
my_dogs = list()

my_dogs.append(Dog())
my_dogs.append(Dog())

for dog in my_dogs:
  dog.bark()