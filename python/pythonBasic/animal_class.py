class Animal(object):
    def __init__(self, name): # __어쩌구__ : 기본 메서드
        self.name = name
    def move(self):
        print("move~")
    def speak(self):
        pass

class Dog(Animal):
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("woof-woof")

class Duck(Animal):
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("quack-quack")

