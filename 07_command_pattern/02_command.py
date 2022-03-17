from abc import ABCMeta, abstractmethod

class Command(metaclass = ABCMeta):
    def __init__(self, recv):
        self.recv = recv
        
    def execute(self):
        pass
    
class ConcreteCommand(Command):
    def __init__(self, recv):
        self.recv = recv
        print('[ConcComand]: ConcreteCommand Initialized!!!!')
        
    def execute(self):
        print('[ConcComand]: Call Receiver.action()')
        self.recv.action()
        
class Receiver:
    def __init__(self):
        print('[Receiver]: Receiver Initialized!')
    def action(self):
        print('[Receiver]: Receiver Action Start')
        
class Invoker:
    def __init__(self):
        print('[Invoker]: Invoker Init!!')
    def command(self, cmd):
        self.cmd = cmd
        print("[Invoker]: 'cmd' is a Class!")
        
    def execute(self):
        print('[Invoker]: Call ConcreteCommand.execute()')
        self.cmd.execute()
        
if __name__ == '__main__':
    recv = Receiver() # Receiver Initialized!
    cmd = ConcreteCommand(recv) # ConcreteCommand Initialized!!!!
    invoker = Invoker() # Invoker Init!!'
    invoker.command(cmd)
    invoker.execute()
    