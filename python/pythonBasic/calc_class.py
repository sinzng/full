class Calc(object):
    def __init__(self, a, b): # __어쩌구__ : 기본 메서드
        self.a = a
        self.b = b

    def add(self):
        return int(self.a)+int(self.b)
    def sub(self):
        return int(self.a)-int(self.b)
