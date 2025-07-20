class myClass:
    __privateVar=27
    def __privMeth(self):
        print("Hello Kiaan")
    def hello(self):
        print("Private Variable Value",myClass.__privateVar)
        #print("Printing private method",myClass.__privMeth())
k= myClass()
k.hello()
k.__privMeth()


    