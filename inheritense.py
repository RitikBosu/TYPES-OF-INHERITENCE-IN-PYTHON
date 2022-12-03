class first:
    def a(self):
        print("first class function")
class second(first):
    def b(self):
        print("second class function")
o=second()
o.a()
o.b()
#untill this is single level inheritense
class third(second):
    def c(self):
        print("third cass function")
l=third()
l.a()
l.b()
l.c()

