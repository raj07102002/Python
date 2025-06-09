# a=1
# b=2
# print(a+b) 

# # Q.1 

# extra_classes=["vocal classes","english","maths","hindi","python","java"]
# print("In the 2021 you will have do this co-curriculam attivites")
# for subject in extra_classes:
#     print(subject) 

# Q.2 

# result=True
# for marks in 65,45,39,16,20:
#     if marks<35:
#         result=False
#         break
#         print(marks) 
#     if (not(result)):
#         print("fail") 

Q.3 
def new(**n):
    print(n)
    print(type(n))
    for k,v in n.items():
        print(f'my key  is {k} and value is={v}')
    for k in n.keys():
        print(f'my key is={k}')
    for v in n.values():
        print(f'my value is={v}')
new(name="Raj",age=22,qulifi="b.tech")