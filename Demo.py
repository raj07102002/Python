class Student:
        school='MHSS'
        gread='10th'
        def __init__(self,name):
                self.n=name 
        def show_details(self,city1,city2,city3):
            print(self.n)
            print(Student.school)
            print(Student.gread) 
        @staticmethod
        def welcome(): 
                 print('welcome')
        @staticmethod
        def thanku():
                print('thanku')
Student.welcome()       
obj=Student('Raj')
#obj.show_details()
#Student.update_gread("11th")
obj2=Student('Ram')
#obj2.show_details()
# Student.add_new()
obj2.show_details('bhopal','indore','jabalpur')
Student.thanku()