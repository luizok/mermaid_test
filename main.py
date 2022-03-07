from typing import List

from src import animal


class Dog(animal.WalkingAnimal):

    def eat(self):
        print('The dog is eating')

    def sleep(self):
        print('The dog is sleeping')


class Eagle(animal.FlyingAnimal):

    def eat(self):
        print('The eagle is eating')

    def sleep(self):
        print('The eagle is sleeping')


class BabyShark(animal.SwimmingAnimal):

    def eat(self):
        print('The baby shark is eating')

    def sleep(self):
        print('The baby shark is sleeping')


if __name__ == '__main__':

    animals: List[animal.AbstractAnimal] = [
        Dog(), Eagle(), BabyShark()
    ]

    for a in animals:
        a.move()
        a.eat()
        a.sleep()
        print('')
