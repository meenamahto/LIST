j=1
l=[]
while j<=1000:
    i=j
    a=i
    sum=0
    while i>0:
        sum=sum+(i%10)*(i%10)*(i%10)
        i=i//10
    if a==sum:
        l.append(a)
    j=j+1
print(l)

