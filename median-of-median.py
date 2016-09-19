import random
import time

def median5(a): #find median size<=5
	n=len(a)
	return sorted(a)[n//2]


def kth(a,k):
    if k==1:
        return min(a)
    n=len(a)
   
    median=[]
    i=0
    while i<n//5:
    	median.append(median5(a[i*5:i*5+5]))
    	i+=1
    if n%5:
    	median.append(median5(a[i*5:]))
    
    if len(median)==1:
    	pivot=a[0]
    else:
    	pivot=kth(median,len(median)//2)
    
    less=filter(lambda x:x<pivot,a)
    nEq=a.count(pivot)
    greater=filter(lambda x:x>pivot,a)
    nL=len(less)
    nG=len(greater)
    if  k<=nL:
        return kth(less,k)
    elif k<=nL+nEq:
        return pivot
    return kth(greater,k-nL-nEq)



