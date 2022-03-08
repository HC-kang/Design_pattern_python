from abc import ABCMeta, abstractclassmethod, abstractmethod
from codeop import Compile

class Compiler(metaclass = ABCMeta):
    @abstractmethod
    def collectSource(self):
        pass
    
    @abstractmethod
    def compileToObject(self):
        pass
    
    @abstractmethod
    def run(self):
        pass
    
    def compileAndRun(self):
        self.collectSource()
        self.compileToObject()
        self.run()
        
class iosCompiler(Compiler):
    def collectSource(self):
        print("Collecting Swift Source Code")
        
    def compileToObject(self):
        print("Compiling Swift code to LLVM bitcode")
        
    def run(self):
        print("Program running on runtime environment")
        
ios = iosCompiler()
ios.compileAndRun()