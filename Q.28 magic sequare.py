
a=[]
for i in range(3):
    b=[]
    for j in range(3):
        j=int(input("Enter your number:"))
        b.append(j)
    a.append(b)
a=[[2,7,6],[9,5,1],[4,3,8]]
print("matrix is......")
for i in range (3):
    for j in range(3):
        print(a[i][j],end=" ")
    print()
sumd1=0
sumd2=0
for i in range(3):
    for j in range(3):
        if i==j:
            sumd1=sumd1+a[i][j]
        if i+j==3-1:
            sumd2=sumd2+a[i][j]
if sumd1!=sumd2:
    f=1
else:
    for i in range(3):
        sumr=0
        sumc=0
    for j in range(3):
        sumr=sumr+a[i][j]
        sumc=sumc+a[j][i]
    if sumr!=sumd1:
        f=1
    elif sumc!=sumd1:
        f=1
    else:
        f=0
if f==0:
    print("matrix is a magic sequare")
else:
    print("matrix is not a magic sequare")


#in while-


a=[[2,7,6],[9,5,1],[4,3,8]]
print("matrix is......")
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        print(a[i][j],end=" ")
        j=j+1
    print()
    i=i+1
i=0
while i<len(a):
    j=0
    sc=0
    sr=0
    while j<len(a[i]):
        sr=sr+a[i][j]
        sc=sc+a[j][i]
        j=j+1
    i=i+1
if sr!=sc:
    f=1
else:
    i=0
    sum=0
    while i<len(a):
        j=0
        sd=0
        while j<len(a[i]):
            if a[i]==a[j]:
                sd=a[i][j]
                sum=sum+sd
            j=j+1
        i=i+1
if sum!=sr:
    f=1
else:
    sum1=0
    for i in range(3):
        for j in range(3):
            if i+j==len(a)-1:
                sum1=sum1+a[i][j]

    if sum1!=sr:
        f=1
    else:
        f=0
if f==0:
    print("matrix is a magic sequare")
else:
    print("matrix is not a magic sequare")
