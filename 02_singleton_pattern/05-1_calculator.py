class Calculator(type):
    def __new__(cls, name, bases, dct):
        dct['help'] = '사칙연산 클래스'
        dct['add'] = lambda self, a, b: a + b
        dct['minus'] = lambda self, a, b: a - b
        dct['divide'] = lambda self, a, b: a / b
        dct['multiple'] = lambda self, a, b: a * b
        return type.__new__(cls, name, bases, dct)
    
Calc = Calculator('Calc', (object,), {})
c = Calc()

print(c.help)
print(c.add(1, 2))
print(c.minus(5, 2))
print(c.divide(8, 2))
print(c.multiple(4, 3))