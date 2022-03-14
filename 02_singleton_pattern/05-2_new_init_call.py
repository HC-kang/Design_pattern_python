class MyMetaClass(type):
    def __new__(cls, *args, **kwargs):
        print("metaclass __new__")
        return super().__new__(cls, *args, **kwargs)
    
    def __init__(cls, *args, **kwargs):
        print("metaclass __init__")
        super().__init__(*args, **kwargs)
        
    def __call__(cls, *args, **kwargs):
        print("metaclass __call__")
        return super().__call__(*args, **kwargs)
    
class MyClass(metaclass = MyMetaClass): 
    def __init__(self):
        print("child __init__")
        
    def __call__(self):
        print("child __call__")
        
print('===========')
obj = MyClass()

"""
result

metaclass __new__
metaclass __init__
===========
metaclass __call__
child __init__

    MyClass 또한 'MyMetaClass'의 객체임. 
    생성되는순간 메타클래스의 __new__, __init__이 실행됨.


"""