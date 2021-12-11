
# buble sort

a=[7,4,5,6,8,9,1,3,2]

for i in range(len(a)-1,0,-1):
    for j in range(i):
        if a[j]>a[j+1]:
            c=a[j]
            a[j]=a[j+1]
            a[j+1]=c
print(a)

