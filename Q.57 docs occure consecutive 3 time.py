a=[4, 5, 5, 5, 3, 8]
i=0
while i<len(a)-2:
    if a[i]==a[i+1] and a[i+1]==a[i+2]:
        print(a[i])
    i=i+1
