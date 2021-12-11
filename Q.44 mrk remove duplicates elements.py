a=[1,1,2,3,2,4,3,5,3,4,3,5,5,2,1]
i=0
b=[]
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
    i=i+1
print(b)




# docs question

List = [1,2,3,1,2,2]
i=0
b=[]
while i<len(List):
    if List[i] not in b:
        b.append(List[i])
    i=i+1
print(b)