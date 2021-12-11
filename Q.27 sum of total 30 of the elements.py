number = 30
n = [10, 11, 12, 13, 14, 17, 18,19]
i=0
b=[]
while i<len(n):
    j=0
    while j<i:
        if n[i]+n[j]==number:
            b.append([n[i],n[j]])
        j=j+1
    i=i+1
print(b)


