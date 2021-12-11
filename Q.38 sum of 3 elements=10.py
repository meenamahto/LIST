a=[1,2,3,4,5,6,7,8,9]
i=0
b=[]
while i<len(a):
    j=0
    while j<i:
        k=0
        while k<j:
            if a[i]+a[j]+a[k]==10:
                b.append([a[i],a[j],a[k]])
            k=k+1
        j=j+1
    i=i+1
print(b)