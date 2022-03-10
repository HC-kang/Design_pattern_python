from lib2to3.pgen2.grammar import Grammar


class GradeMap:
    _instance = None

    @classmethod
    def _getInstance(cls):
        return cls._instance

    @classmethod
    def instance(cls, *args, **kargs):
        cls._instance = cls(*args, **kargs)
        cls.instance = cls._getInstance
        return cls._instance

    def __init__(self):
        self._dict = {}

    def setitem(self, key, item):
        self._dict[key] = item
        
        
class Student:
    def __init__(self, age, name, korean, mathematics, english):
        self._age = age
        self._grade = GradeMap.instance().get_grade(age)

    @property
    def age(self):
        return self._age

    @property
    def grade(self):
        return self._grade

        
a = Student()
a.grade = 70
a.grade
a.get_grade()

id(a)

b = Student()
b.grade.get_grade()
id(b)