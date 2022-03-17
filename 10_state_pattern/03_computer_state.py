# Abstract Class
class ComputerState():
    name = 'state'
    allowed = []
    
    def switch(self, state):
        if state.name in self.allowed:
            print('Current:', self, '=> switched to new state', state.name)
            self.__class__ = state
        else:
            print('Current:', self, '=> switching to', state.name, 'not possible.')

    def __str__(self):
        return self.name

# Concrete Class
class Off(ComputerState):
    name = 'off'
    allowed = ['on']
    
class On(ComputerState):
    name = 'on'
    allowed = ['off', 'suspend', 'hibernate']
    
class Suspend(ComputerState):
    name = 'suspend'
    allowed = ['on']
    
class Hibernate(ComputerState):
    name = 'hibernate'
    allowed = ['on']
    
# Context Class
class Computer():
    def __init__(self, model = 'HP'):
        print('I just bought a new computer!!')
        self.model = model
        self.state = Off()
        
    def change(self, state):
        self.state.switch(state)

if __name__ == '__main__':
    comp = Computer()
    
    comp.change(On)
    
    comp.change(Off)
    
    comp.change(On)
    
    comp.change(Suspend)
    
    comp.change(Hibernate)
    
    comp.change(On)
    
    comp.change(Off)