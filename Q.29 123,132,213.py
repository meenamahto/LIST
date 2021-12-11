a=[1,2,3]
i=0
while i<len(a):
    j=0
    while j<len(a):
        k=0
        while k<len(a):
            if i!=j and j!=k and i!=k:
                print(a[i],a[j],a[k])
            k=k+1
        j=j+1
    i=i+1

# in for loop

a=[1,2,3]
for i in range(3):
    for j in range(3):
        for k in range(3):
            if i!=j and j!=k and k!=i:
                print(a[i],a[j],a[k])



a=[0,9,5]
i=0
while i<len(a):
    j=0
    while j<len(a):
        k=0
        while k<len(a):
            if i!=j and j!=k and k!=i:
                print(a[i],a[j],a[k])
            k=k+1
        j=j+1
    i=i+1




