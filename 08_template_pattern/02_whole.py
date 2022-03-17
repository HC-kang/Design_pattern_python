from abc import ABCMeta, abstractmethod

class AbstractClass(metaclass = ABCMeta):
    def __init__(self):
        pass
    
    @abstractmethod
    def operation1(self):
        pass
    
    @abstractmethod
    def operation2(self):
        pass
    
    @abstractmethod
    def thisIsHook(self):
        pass
    
    def template_method(self):
        print("Defining the Algorithm. Operation1 follows Operation2")
        self.operation2()
        self.operation1()
        self.thisIsHook()
        
class ConcreteClass(AbstractClass):
    def operation1(self):
        print("my Concrete Operation1")
    
    def operation2(self):
        print("operation2 remains same")
        
    def thisIsHook(self):
        choice = input("Do you want to repeat?(Y/N)")
        if choice == 'Y':
            self.operation2()
            self.operation1()
            
class Client:
    def main(self):
        self.concrete = ConcreteClass()
        self.concrete.template_method()
        
client = Client()
client.main()