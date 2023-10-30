class Parents:
    def grandfather(self):
        print("My grandfather name is Ram.")

class Father(Parents):
        def father(self):
            print("My father name is Dibya.")

class Daughter(Parents):
        def daughter(self):
            print("I am Dishna Koirala.")

s=Daughter()
s.daughter()
s.grandfather()

print("....................")
class A:
    def a(self):
        print("I am from Nepal.")

class B(A):
    def b(self):
        print("I am from America.")

class C(A):
    def c(self):
        print("I am from India.")

b = B()
b.a()
b.b()

c=C()
c.a()