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