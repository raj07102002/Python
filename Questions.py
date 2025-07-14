# Q1. 

# if n % 2 == 1:
#     print("Weird")
# elif n % 2 == 0 and 2 <= n <= 5:
#     print("Not Weird")
# elif n % 2 == 0 and 6 <= n <= 20:
#     print("Weird")
# elif n % 2 == 0 and n > 20:
#     print("Not Weird") 

# Q.2 

# if __name__ == '__main__':
#     n = int(input())
#     for i in range(1, n + 1):
#         print(i, end='')

# Q.3 

# n = int(input())
# if n < 2:
#     print("Not Prime")
# else:
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime") 

# Q.4 

# class Dog:
#     def speak(self):
#         return "Dog says Woof"

# class Cat:
#     def speak(self):
#         return "Cat says Meow"

# class Cow:
#     def speak(self):
#         return "Cow says Moo"

# # Common interface
# def animal_sound(animal):
#     print(animal.speak())

# # Call with different objects
# dog = Dog()
# cat = Cat()
# cow = Cow()

# animal_sound(dog)   # Output: Dog says Woof
# animal_sound(cat)   # Output: Cat says Meow
# animal_sound(cow)   # Output: Cow says Moo

# Q.5 

# n = 5
# if n < 2:
#     print("Not Prime")
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime")  # Output: Prime  

# Q.6 

# n = 123
# total = 0
# while n > 0:
#     digit = n % 10
#     total += digit
#     n = n // 10
# print(total) 

# Q.7

# n = 123
# total = 0
# while n > 0:
#     digit = n % 10
#     total += digit
#     n = n // 10
# print(total) 

# Q.8 

# s = "apple"
# vowels = "aeiou"
# count = 0
# for char in s:
#     if char in vowels:
#         count += 1
# print(count)  

Q.9 

# class Car:
#     # Constructor
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     # Method
#     def show_details(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)

# # Create Object
# car1 = Car("Toyota", "Innova")
# car2 = Car("Tata", "Punch")

# # Call method
# car1.show_details()
# car2.show_details()