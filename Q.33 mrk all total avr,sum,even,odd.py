
elt = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
count=0
sum=0
sume=0
sumo=0
even=0
odd=0
i=0
while i<len(elt):
    count=count+1
    sum=sum+elt[i]
    if elt[i]%2==0:
        even=even+1
        sume=sume+elt[i]
    else:
        odd=odd+1
        sumo=sumo+elt[i]
    i=i+1
print("total even=",even)
print("total odd=",odd)
print("total elements=",count)
print("sum of even=",sume)
print("sum of odd=",sumo)
print("sum of elements=",sum)
print("average of even=",sume//even)
print("average of odd=",sumo//odd)
print("average of total elements=",sum//count)
