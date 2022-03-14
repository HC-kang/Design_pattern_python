class Singleton:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

s1 = Singleton()
print('Object created', s1) # __main__.Singleton at 0x7fbdd86137c0>

s2 = Singleton()
print('Object created', s2) # __main__.Singleton at 0x7fbdd86137c0>

s1 is s2 # True