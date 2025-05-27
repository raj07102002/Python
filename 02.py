from abc import ABC,abstractmethod 
class Senior(ABC):
        def add(self,x,y):
                print(x+y)
        def sub(self,x,y):
                print(x-y) 
        def multi(self,x,y):
                print(x*y) 
        @abstractmethod 
        def div(self): 
            pass 
class Junior(Senior):
        def div(self,x,y):
                print(x/y)
obj=Junior()
# obj.add()
# obj.sub()
# obj.multi()
obj.div(4,3)