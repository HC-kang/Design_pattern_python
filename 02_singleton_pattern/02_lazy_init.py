class Singleton:
    __instance = None
    
    def __init__(self):
        if not Singleton.__instance:
            print('__init__ method called..')
        else:
            print('Instance already created:', self.getInstance())
            
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance

s1 = Singleton() # __init__ method called.. but didn't created
print('Object created', Singleton.getInstance()) # object created
s2 = Singleton() # instance already created

s1 is s2 # False...?

s1 = Singleton.getInstance()
s2 = Singleton.getInstance()

s1 is s2 # True, getInstance에서 비로소 __instance가 생성됨.


'''
Singleton 클래스 열어보기
'''
class Singleton:
    instance = None
    
    def __init__(self):
        if not Singleton.instance:
            print('__init__ method called..')
        else:
            print('Instance already created:', self.getInstance())
            
    @classmethod
    def getInstance(cls):
        if not cls.instance:
            cls.instance = Singleton()
        return cls.instance

s1.instance.instance.instance.instance #...