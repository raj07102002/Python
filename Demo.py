# class Student:
#         school='MHSS'
#         gread='10th'
#         def __init__(self,name):
#                 self.n=name 
#         def show_details(self,city1,city2,city3):
#             print(self.n)
#             print(Student.school)
#             print(Student.gread) 
#         @staticmethod
#         def welcome(): 
#                  print('welcome')
#         @staticmethod
#         def thanku():
#                 print('thanku')
# Student.welcome()       
# obj=Student('Raj')
# #obj.show_details()
# #Student.update_gread("11th")
# obj2=Student('Ram')
# #obj2.show_details()
# # Student.add_new()
# obj2.show_details('bhopal','indore','jabalpur')
# Student.thanku() 
 
#  Q.2 

#  class Student:
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

# Q.3 
Pen_count=10
Pen_taken=0
while(Pen_count>0):
    Pen_taken=2
    Pen_count=Pen_count-Pen_taken
print("number of pen taken in stand=",Pen_count)
