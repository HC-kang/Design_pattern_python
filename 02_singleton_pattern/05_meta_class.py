class MyInt(type):
    def __call__(cls, *args, **kwargs):
        print("***** Here's My int *****", args)
        return type.__call__(cls, *args, **kwargs)
    
class Int(metaclass = MyInt):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

i = Int(4, 5) 
"""
Int class를 활용하면, 자동으로 MyInt class의 __call__ 메소드가 호출된다.
"""
