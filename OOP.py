class Animal:
    def _init_(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Cow(Animal):
    def speak(self):
        return "Moo!"

def animal_speak(animal):
    print(animal.speak())

dog = Dog("Rufus")
cat = Cat("Whiskers")
cow = Cow("Betsy")

animal_speak(dog)
animal_speak(cat)
animal_speak(cow)