a=[[1,2,3,],[4,5,6],[7,8,9]]
i=0
b=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        b.append(a[i][j])
        j=j+1
    i=i+1
print(b)