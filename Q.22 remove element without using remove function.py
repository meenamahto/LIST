a=[11,22,33,44]
a[2:3]=[]
print(a)

a=[11,22,33,44]
b=[]
i=0
while i<len(a):
    if a[i]!=33:
        b.append(a[i])
    i=i+1
print(b)