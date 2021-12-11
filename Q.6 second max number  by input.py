a=[]
s=int(input("Enter your number of size:"))
b=1
while b<=s:
    n=int(input("Enter your number what you want in the list :"))
    a.append(n)
    b=b+1
print(a)
i=0
max=0
while i<len(a):
    if a[i]>max:
        max=a[i]
    i=i+1
i=0
max2=0
while i<len(a):
    if a[i]>max2:
        if a[i]!=max:
            max2=a[i]
    i=i+1
print(max2)


