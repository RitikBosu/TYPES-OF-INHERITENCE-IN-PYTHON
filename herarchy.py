class first:
    def a(self):
        print("first class function")
class second(first):
    def b(self):
        print("second class function")


class third(first):
    def c(self):
        print("third cass function")
o=second()
o.a()
o.b()
#heirachy inheritence
l=third()
l.a()
l.c()

