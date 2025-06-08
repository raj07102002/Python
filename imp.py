# Q.1
# s=set()
# s.add(20)
# s.add(20.)
# s.add("20")
# print(len(s)) 

# Q.2 
# d={}
# name=input("Enter the name :")
# lang=input("Enter the lang :")
# d.update({name:lang}) 

# name=input("Enter the name :")
# lang=input("Enter the lang :")
# d.update({name:lang}) 

# name=input("Enter the name :")
# lang=input("Enter the lang :")
# d.update({name:lang}) 


# # name=input("Enter the name :")
# # lang=input("Enter the lang :")
# # d.update({name:lang}) 

# # name=input("Enter the name :")
# # lang=input("Enter the lang :")
# # d.update({name:lang}) 

# print(d)  
# Q.3
# a=int(input("Enter the value:")) 

# if(a>=18): 
#     print("yes i am 18 above") 

# elif(a<0): 
#     print("IT a negtive number")
#     print("There is no meaning you enter this value")
#     print("Try again") 
# elif(a==0):
#     print("Try again") 
# else: 
#     print("invalid") 
# print("End the program") 

# Q.4 

# n=int(input("enter any value = "))
# x=y=n
# digit=0
# sum=0
# while n>0: 
#     digit=digit+1
#     n=n//10
# print(digit)
# print(n)
# while x>0: 
#     last_digit=x%10
#     sum=sum+last_digit**digit
#     x=x//10
# print(sum)
# print(x)
# if y==sum: 
#     print(f'given no. {y} is armstrong no.')
# else: 
#     print(f'given no. {y} is not a armstrong no.') 

# Q.4 
# def new(**n):
#     print(n)
#     print(type(n))
#     for k,v in n.items():
#         print(f'my key  is {k} and value is={v}')
#     for k in n.keys():
#         print(f'my key is={k}')
#     for v in n.values():
#         print(f'my value is={v}')
# new(name="Raj",age=22,qulifi="b.tech") 

# Q .5 

# n=int(input("Enter any value="))
# i=0
# while i<n: 
#     print(" "*(n-i)+" *"*i)
#     i=i+1
# print(i)
# i=i-2
# while i>=0: 
#     print(" "*(n-i)+" *"*i)
#     i=i-1 

# Q.6 
# n=int(input("Enter any value="))
# i=0
# while i<n: 
#     print(" "*i+" *"*(n-i))
#     i=i+1
# # print(i)
# i=i-2
# while i>=0: 
#     print(" "*i+" *"*(n-i))
#     i=i-1 

# Q.7 armstrong 

# n=int(input("enter any value = "))
# x=y=n
# digit=0
# sum=0
# while n>0: 
#     digit=digit+1
#     n=n//10
# print(digit)
# print(n)
# while x>0: 
#     last_digit=x%10
#     sum=sum+last_digit**digit
#     x=x//10
# print(sum)
# print(x)
# if y==sum: 
#     print(f'given no. {y} is armstrong no.')
# else: 
#     print(f'given no. {y} is not a armstrong no.')

# Q.8 

# while True: 
#     print("1.add\n2.sub\n3.mult\n4.div\n5off")
#     n=int(input("Enter any option: "))
#     x=(1,2,3,4,5)
#     if n in x: 
#         if n in (1,2,3,4): 
#             a=int(input("Enter 1st value: "))
#             b=int(input("Enter 2nd value: "))
#         if n==1: 
#             print("The answer is = ",a+b)
#         elif n==2: 
#             print("The answer is = ",a-b)
#         elif n==3: 
#             print("The answer is = ",a*b)
#         elif n==4: 
#             print("The answer is = ",a/b)
#         elif n==5: 
#             break
#     else: 
#         print("please enter valid option") 

# Q.9 oops 
# class Student :
#         def __init__(self,name,city,phone):
#             self.n=name
#             self.c=city
#             self.p=phone
# # obj=student
# # print(obj.n,obj.c,obj.p)
# obj=Student('Raj','Bhopal',9098216203)
# obj1=Student('ram','seoni',7648913604)
# obj2=Student('shyam','Bhopal',9098216203)
# print(obj.n,obj1.c,obj1.p)
# print(obj1.n,obj1.c,obj1.p)
# print(obj2.n,obj2.c,obj2.p) 

# Q.10
for i in range(2,10):
    if(i%2!=0): 
        break
    print(i)
