# a=(3,2,5,2,2) 

# print(a.count(2)) 

Q.2 def factorial(n): 
    fact=1
    for i in range(1,n+1): 
        if i>0: 
            fact*=i
    print(fact)
x=int(input("Enter any value = "))
factorial(x)