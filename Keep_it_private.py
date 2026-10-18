class myclass:
    
    __privateVar = 27;
    
    def __privateMeth(self):
        print("i'm inside class")

    def Hello(self):
        print("Private variabel value:", myclass.__privateVar)

foo = myclass
foo.Hello
foo.__privateMeth