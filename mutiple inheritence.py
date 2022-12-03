class first:
    def a(self):
        print("first class function")
class second:
    def b(self):
        print("second class function")
class third(first,second):
    def c(self):
        print("im in third cass function")
l=third()
l.a()
l.b()
l.c()