a=[8,2,3,4,5,6]
i=0
b=[]
c=0
d=0
while i<len(a):
    if i==0:
        b=a[i]
    if i==len(a)-1:
        c=a[i]
    i=i+1
print("first element=",b)
print("last element=",c)


a=[12,34,65,4,3,21]
i=0
b=[]
while i<len(a):
    if a[i]==21:
        b.insert(0,a[i])
    elif a[i]==3:
        b.insert(0,a[i])
    elif a[i]!=21 and a[i]!=3:
        b.append(a[i])
    i=i+1
print(b)
