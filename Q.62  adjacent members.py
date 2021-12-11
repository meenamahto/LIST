# a=['1', '2', '3', '4', '5', '6', '7', '8']
a=["1","2","3"]
i=0
b=[]
while i<len(a)-1:
    b.append(a[i]+a[i+1])
    a.remove(a[i])
    i=i+1
print(b) 