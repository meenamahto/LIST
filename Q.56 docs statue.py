a=[6, 2, 3, 8]
i=0
c=0
while i<len(a):
    j=0
    while j<len(a)-1:
        if a[j]>a[j+1]:
            c=a[j]
            a[j]=a[j+1]
            a[j+1]=c
        j=j+1
    i=i+1
print("previous statue=",a)
i=0
b=[]
while i<len(a):
    b.append(a[i]+1)
    i=i+1
print("next statue=",b)

