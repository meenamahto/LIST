print([i for i in range(1,11) if i%2==0])

print([i**2 if i%2==0 else i**3 for i in range(1,11)])



list1=[1,2,3,4]
list2=[1,20,30,4]
# result=[i for i in list1 for j in list2 if i==j]
# print(result)
print([i for i in list1 for j in list2 if i==j])



b=[]
for i in list1:
    for j in list2:
        if i==j:
            b.append(j)
print(b)