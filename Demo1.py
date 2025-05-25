class Student :
        def __init__(self,name,city,phone):
            self.n=name
            self.c=city
            self.p=phone
# obj=student
# print(obj.n,obj.c,obj.p)
obj=Student('Raj','Bhopal',9098216203)
obj1=Student('ram','seoni',7648913604)
obj2=Student('shyam','Bhopal',9098216203)
print(obj.n,obj1.c,obj1.p)
print(obj1.n,obj1.c,obj1.p)
print(obj2.n,obj2.c,obj2.p)