class first:
    def a(self):
        print("first class function")
class second(first):
    def b(self):
        print("second class function")
#this is hybrid inheritense
class third(second):
    def c(self):
        print("third cass function")
class fourth(second,first):
    def d(self):
        print("im in fourth")
        
    
l=fourth()
l.a()
l.b()


