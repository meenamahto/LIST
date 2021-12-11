s=int(input("Enter your start value:"))
s=1
e=int(input("Enter your second value:"))
e=10
l=[]
for i in range (s,e+1):
    a=0
    for j in range(2,i):
        if i%j==0:
            a=1
    if a==0:
        l.append(i)
print(l,end=" ")
# print("prime number in",s,"to",e)




# import random


# a="python"
# b=list(a)
# for i in range(len(a)):
#     one=random.randint(0,len(a)-1)
#     second=random.randint(0, len(a)-1)
#     b[one], b[second]=b[second], b[one]

# print(str(b))




