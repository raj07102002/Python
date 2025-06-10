# i=0
# while i<5 : 
#     print("Raj",end=",")
#     i+=1 

# Q.1 

# l=['1','Raj','lakshman','janki','jai bolo hanuman ki']
# i=0
# while i<(len(l)): 
#     print(l[i])
#     i+=1 

# Q.2 
# l=[1,23,54,45]
# for item in l:
#     print(item)
# else: 
#     print("done")

# Q.3 
# for i in range(0, 50):
#     if i < 34:
#         continue
#     print(i) 

# Q.4  
# l=["Rahul","Ram","sita","shiva"] 
# for name in l: 
#     if(name.startswith("R")):
#         print(f"Hey{name}") 

# Q.5 

# class Student:
#         def __init__(self,name,city):
#             self.n=name
#             self.c=city
#             print(self.n,self.c) # Access in-side constructor   
#         def add(self,phone):
#             self.p=phone
#             print(self.n,self.c,self.p,self.school)
# obj=Student('Raj','Seoni')
# obj.school='MHSS'
# obj.add(9098216203)
# # print(obj.n,obj.c,obj.p,obj.school) 

Q.6 
class Student:
        def __init__(self,name,city):
            self.n=name
            self.c=city
            print(self.n,self.c) # Access in-side constructor
        def add(self,phone):
            self.p=phone
            print(self.n,self.c,self.p,self.school)
obj=Student('Raj','Seoni')
obj.add(9098216203)
obj.school='MHSS'
# obj.add(9098216203)
print(obj.n,obj.c,obj.p,obj.school)