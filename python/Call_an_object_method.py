class MyClass(object):
    @classmethod
    def myClassMethod(self, x):
        pass
    @staticmethod
    def myStaticMethod(x):
        pass
    def myMethod(self, x):
        return 42 + x

myInstance = MyClass()

myInstance.myMethod(someParameter)

MyClass.myMethod(myInstance, someParameter)


MyClass.myClassMethod(someParameter)
MyClass.myStaticMethod(someParameter)

myInstance.myClassMethod(someParameter)
myInstance.myStaticMethod(someParameter)
