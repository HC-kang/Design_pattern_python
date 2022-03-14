class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        print('MetaSingleton was called..')
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    
class Logger(metaclass = MetaSingleton):
    def __init__(self, x):
        self.x = x
        print('Logger is created!!!')
        print(f'Number is {x}')

logger1 = Logger(3)
logger2 = Logger(5)

logger1.x # 3
logger2.x # 3

print(logger1 is logger2)