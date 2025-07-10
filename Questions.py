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
