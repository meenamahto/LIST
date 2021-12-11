a= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(a[i+1]-a[i] for i in range(len(a)-1) ))

b=[]
i=0
while i<len(a)-1:
    b.append(a[i+1]-a[i]) 
    i=i+1
print(b)
