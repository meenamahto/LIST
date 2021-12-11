a=[1,4,5,6,10,7,8,9,23,]
i=0
count=0
sum=0
sum1=0
while i<len(a):
    count=count+1
    # i=i+1
    if count%2==0:
        sum=sum+a[i]
    else:
        sum1=sum1+a[i]
    i=i+1
print(sum)
print(sum1)

a=["meena","anjali","ankita"]
i=0
count=0
while i<len(a):
    if type[a] is list:
        count=count+1
    i=i+1
print(str(count))



