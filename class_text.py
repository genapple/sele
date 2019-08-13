class A(object):
    def __init__(self,a,b):
        self.a=int(a)
        self.b=int(b)
    def add(self):
        return self.a+self.b
class B(A):
    def sub(self):
        return self.a-self.b
count=A('4',5)
count1=B(4,5)
print count1.add()
# print count.add()
