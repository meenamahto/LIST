a=[]
s=int(input("Enter your number of size:"))
b=1
while b<=s:
    n=int(input("Enter your number what you want in the list"))
    a.append(n)
    b=b+1
i=0
max=0
while i<len(a):
    if a[i]>max:
        max=a[i]
    i=i+1
a.remove(max)
max2=0
i=0
while i<len(a):
    if a[i]>max2:
        max2=a[i]
    i=i+1
a.remove(max2)
i=0
max3=0
while i<len(a):
    if a[i]>max3:
        max3=a[i]
    i=i+1
print(max3)
