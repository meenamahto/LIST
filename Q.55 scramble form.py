a=["meena","arpita","sakshi","anjali","pooja","kavita"]
i=0
d=[]
while i<len(a):
    j=0
    b=a[i][0:2]
    c=a[i][2:]
    while j<len(a[i]):
        d.append(c+b)
        j=j+1
        break
    i=i+1
print(d)

