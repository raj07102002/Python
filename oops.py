class Parent:
    x=10 
    def __init__(self,name):
        self.name=name 
        
    def home(self): 
        print("home from parent class")
        
class Child1(Parent):
    
    def home(self):
        
        print("home from Child class") 
        
        super().home()
class child2(Parent): 
        pass

obj1=Child1("Python")
obj2=child2("java")
obj1.home()
obj2.home()
print(obj1.name,obj2.name)
# print(obj.x)
# print(obj.name)
# obj.home()
# obj.car()