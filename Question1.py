# Q.1
# import pyttsx3
# engine = pyttsx3.init()

# # For Mac, If you face error related to "pyobjc" when running the `init()` method :
# # Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

# engine.say("hello raj chandrawashi me i help you")
# engine.runAndWait() 

# Q.2 

# import os

# # Set the directory path (you can also use "." for current directory)
# directory_path = "."

# # Get the list of files and folders
# contents = os.listdir(directory_path)

# # Print the contents
# print(f"Contents of '{directory_path}':")
# for item in contents:
#     print(item) 

# Q.3 
# a="12.4" 
# b=int(float(a))
# print(type(b))  
# class type(int)
# a="12"
# b=int(a)
# print(type(b)) 
# class type(int) 

# Q.4 

# a = "12.4"

# try:
#     b = int(a)
# except ValueError:
#     print(f"'{a}' is not a valid integer directly!")

# # Now convert safely
# b = int(float(a))
# print("Converted:", b) 

# Q.5 
# class Student:
#     def __init__(self, name):
#         self.__name = name  # Private variable

#     def get_name(self):
#         return self.__name

# s = Student("Raj")
# print(s.get_name())

# Q.6 

# class Animal:
#     def speak(self):
#         print("Animal speaks")

# class Dog(Animal):
#     def speak(self):
#         print("Dog barks")

# class Cat(Animal):
#     def speak(self):
#         print("Cat meows")

# # Polymorphism in action
# for animal in [Dog(), Cat(), Animal()]:
#     animal.speak() 

# Q.7 

# class student: 
#     def __init__(self, name, grade): 
#         self.name = name 
#         self.grade = grade

#     def get_grade(self):  # ✅ Fix: no double underscore
#         return f'{self.name} is in grade {self.grade}'

# student1 = student("raj", 1)
# print(student1.get_grade())  # ✅ Works fine