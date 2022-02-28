from tokenize import Single


class Singleton:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

s = Singleton()
print('Object created', s)

s1 = Singleton()
print('Object created', s1)

# class NotSingleton:
#     def __init__(self):
#         if not hasattr(self, 'instance'):
#             self.instance = super(NotSingleton, self).__init__(self)
#         return self.instance
    
# n = NotSingleton()
# print('Object created', n)

# n1 = NotSingleton()
# print('object created', n1)