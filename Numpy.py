import numpy as np 
import time 
size=10000000
l1=range(size)
l2=range(size)
start=time.time()
result=[x+y for x,y in zip(l1,l2)] 
end =time.time() 
print("python list is: ",end -start) 

a1=np.arange(size)
a2=np.arange(size)
start=time.time()
result=a1+a2
end=time.time()
print("python array :",end - start)