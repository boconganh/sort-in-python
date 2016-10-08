

def k_mergesort(arrs):
    n=0
    k=len(arrs)
    for i in range(k):
        n+=len(arrs[i])
    ans=[0]*n
    lastIndex=[0]*k
    for i in range(n):
        minIndex=-1
        minValue=0
        for j in range(k):
            if lastIndex[j]<len(arrs[j]):
                if minIndex<0 or arrs[j][lastIndex[j]]<minValue:
                    minIndex=j
                    minValue=arrs[j][lastIndex[j]]
        lastIndex[minIndex]+=1
        ans[i]=minValue
    return ans

def mergesort(a,k=4):
    n=len(a)
    if n<2:
        return
    arrs=[[] for i in range(k)]
    for i in range(n):
        arrs[i%k].append(a[i])
    for i in range(k):
        mergesort(arrs[i],k)
    a[:]=k_mergesort(arrs)
    
