class Borg:
    __shared_state = {"1": "2"}
    
    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state
        pass
    
b = Borg()
b1 = Borg()
b.x = 4

print("Borg Object 'b'", b)
print("Borg Object 'b1'", b1) # 두 객체는 다른 객체임
print("Object State 'b':", b.__dict__)
print("Object State 'b1':", b1.__dict__) # 'x': 4

b.x = 10

print("Object State 'b':", b.__dict__) # 'x': 10
print("Object State 'b1':", b1.__dict__) # 그러나 상태를 공유하고있음