from abc import ABCMeta, abstractmethod

# Abstract Factory

class PizzaFactory(metaclass = ABCMeta):
    
    @abstractmethod
    def createVegPizza(self):
        pass
    
    @abstractmethod
    def createNonVegPizza(self):
        pass

# ConcreteFactory1
class IndianPizzaFactory(PizzaFactory):
    
    def createVegPizza(self):
        return DeluxVegPizza()
    
    def createNonVegPizza(self):
        return ChickenPizza()
    
# ConcreteFactory2
class USPizzaFactory(PizzaFactory):
    
    def createVegPizza(self):
        return MexicanVegPizza()
    
    def createNonVegPizza(self):
        return HamPizza()
    
# Abstract Product1
class VegPizza(metaclass = ABCMeta):
    
    @abstractmethod
    def prepare(self, VegPizza):
        pass

# Abstract Product2
class NonVegPizza(metaclass = ABCMeta):
    
    @abstractmethod
    def serve(self, VegPizza):
        pass

# Concrete product1    
class DeluxVegPizza(VegPizza):
    def prepare(self):
        print("Prepare", type(self).__name__)
        
# Concrete product2
class ChickenPizza(NonVegPizza):
    def serve(self, VegPizza):
        print(type(self).__name__, "is served with Chicken on", type(VegPizza).__name__)
        
# Concrete product3
class MexicanVegPizza(VegPizza):
    def prepare(self):
        print("Prepare", type(self).__name__)

# Concrete product4
class HamPizza(NonVegPizza):
    def serve(self, VegPizza):
        print(type(self).__name__, "is served with Ham on ", type(VegPizza).__name__)
        

class PizzaStore:
    def __init__(self):
        pass
    
    def makePizza(self):
        for factory in [IndianPizzaFactory(), USPizzaFactory()]:
            self.factory = factory
            self.NonVegPizza = self.factory.createNonVegPizza()
            self.VegPizza = self.factory.createVegPizza()
            self.VegPizza.prepare()
            self.NonVegPizza.serve(self.VegPizza)
            
pizza = PizzaStore()
pizza.makePizza()