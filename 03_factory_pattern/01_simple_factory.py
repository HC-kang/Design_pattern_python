from abc import ABCMeta, abstractmethod

class Animal(metaclass = ABCMeta):
    @abstractmethod
    def do_say(self):
        pass

class Dog(Animal):
    def do_say(self):
        print("멍멍!")
        
class Cat(Animal):
    def do_say(self):
        print("야옹")
        
class Fox(Animal):
    def do_say(self):
        print("..?")
        
## forest factory
class ForestFactory(object):
    def __init__(self):
        print('[ForestFactory]: FF Initialized!')
    def make_sound(self, object_type):
        print(f'[ForestFactory]: Call subclass ({object_type}) of Animals!!')
        return eval(object_type)().do_say()
                # Dog().do_say()
    
if __name__ == '__main__':
    ff = ForestFactory()
    animal = input("어떤 동물일까?")
    ff.make_sound(animal)
