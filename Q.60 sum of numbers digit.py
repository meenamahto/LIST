a=[12, 67, 98, 34]
i=0
b=[]
while i<len(a):
    rem=a[i]%10
    c=a[i]//10
    sum=rem+c
    b.append(sum)
    i=i+1
print(b)