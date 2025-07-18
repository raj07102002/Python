# class Parent:
#     x=10 
#     def __init__(self,name):
#         self.name=name 
        
#     def home(self): 
#         print("home from parent class")
        
# class Child1(Parent):
    
#     def home(self):
        
#         print("home from Child class") 
        
#         super().home()
# class child2(Parent): 
#         pass

# obj1=Child1("Python")
# obj2=child2("java")
# obj1.home()
# obj2.home()
# print(obj1.name,obj2.name)
# # print(obj.x)
# # print(obj.name)
# # obj.home()
# # obj.car() 

# Q.1 

# class Person:
#     # Constructor (Encapsulation)
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age  # private attribute

#     def display(self):  # Method
#         print(f"Name: {self.name}, Age: {self.__age}")

#     def get_age(self):  # Encapsulation
#         return self.__age

#     def set_age(self, age):  # Setter with validation
#         if age > 0:
#             self.__age = age 

# Q.2 

# # . Inheritance
# class Student(Person):
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)  # Call parent constructor
#         self.student_id = student_id 

# Q.3 

# # 3. Polymorphism: method overriding
#     def display(self):
#         print(f"Student: {self.name}, ID: {self.student_id

# Q.4 

# # . Abstraction using Abstract Base Class
# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

# # ---- Using the classes ----
# p1 = Person("John", 30)
# p1.display()

# s1 = Student("Alice", 20, "S123")
# s1.display()

# r = Rectangle(10, 5)
# print("Area of rectangle:", r.area()) 

# Q.5 

# class Account:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance  # Private attribute

#     def deposit(self, amount):
#         self.__balance += amount

#     def get_balance(self):
#         return self.__balance

# acc = Account("Raj", 1000)
# acc.deposit(500)
# print(acc.get_balance()) 

# Q.6 

# class Cat:
#     def speak(self):
#         return "Meow"

# class Dog:
#     def speak(self):
#         return "Woof"

# # Same interface
# def animal_sound(animal):
#     print(animal.speak())

# animal_sound(Cat())  # Output: Meow
# animal_sound(Dog())  # Output: Woof 

# Q.7 

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return "Makes a sound"

# # Derived Class
# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} says Woof"

# dog = Dog("Tommy")
# print(dog.speak())  # Output: Tommy says Woof