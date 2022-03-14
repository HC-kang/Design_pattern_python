class Borg:
    _shared_state = {}
    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj
    

b1 = Borg()
b2 = Borg()
b1.x = 4

print("Borg Object 'b1'", b1)
print("Borg Object 'b2'", b2) # 두 객체는 다른 객체임
print("Object State 'b1':", b1.__dict__)
print("Object State 'b2':", b2.__dict__) # 'x': 4

b1.x = 10

print("Object State 'b1':", b1.__dict__) # 'x': 10
print("Object State 'b2':", b2.__dict__) # 그러나 상태를 공유하고있음