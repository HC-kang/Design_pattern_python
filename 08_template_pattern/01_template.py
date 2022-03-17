from abc import ABCMeta, abstractclassmethod, abstractmethod
from codeop import Compile

# Abstract Class
class Compiler(metaclass = ABCMeta):
    # template_method()
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
        
# Concrete Class
class iosCompiler(Compiler):
    def collectSource(self):
        self.someOtherMethod()
        print("Collecting Swift Source Code")
        
    def compileToObject(self):
        print("Compiling Swift code to LLVM bitcode")
        
    def someOtherMethod(self):
        print("Some Additional Method")
        
    def run(self):
        print("Program running on runtime environment")
        
ios = iosCompiler()
ios.compileAndRun()