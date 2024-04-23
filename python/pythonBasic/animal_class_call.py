#!/usr/bin/env python

from animal_class import *

dog = Dog('doggy')
print(dog.name)
dog.move()
dog.speak()

duck = Duck('donald')
print(duck.name)
duck.move()
duck.speak()

zoo = [Dog('marry'), Duck('dduck')]

for z in zoo:
    print(z.name)
    z.speak()