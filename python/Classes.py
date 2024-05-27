
class MyClass:
    name2 = 2 

    def __init__(self):
        """
        Constructor  (Technically an initializer rather than a true "constructor")
        """
        self.name1 = 0 
  
    def someMethod(self):
        """
        Method
        """
        self.name1 = 1
        MyClass.name2 = 3
  
  
myclass = MyClass() 

class MyOtherClass:
    count = 0  
    def __init__(self, name, gender="Male", age=None):
        """
        One initializer required, others are optional (with different defaults)
        """
        MyOtherClass.count += 1
        self.name = name
        self.gender = gender
        if age is not None:
            self.age = age
    def __del__(self):
        MyOtherClass.count -= 1

person1 = MyOtherClass("John")
print(person1.name, person1.gender)  
print(person1.age)                   
person2 = MyOtherClass("Jane", "Female", 23)
print(person2.name, person2.gender, person2.age)
