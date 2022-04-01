# HomeWork 8,6

class Test:

    def __init__(self):
        self.a = 0
        self.b = 1
        self.c = 2

    def test1(self):
        pass


test = Test()
m = 'test1'
print(test.__dict__)
print(test.__class__.__dict__[m](test))
