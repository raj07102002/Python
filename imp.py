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