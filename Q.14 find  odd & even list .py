# a = [50, 40, 23, 70, 56, 12, 5, 10, 7]
a=[]
i=0
b=1
x=[]
y=[]
while b<=10:
    n=int(input("Enter your number:"))
    a.append(n)
    b=b+1
i=0
odd=0
even=0
while i<len(a):
    if a[i]%2==0:
        even=a[i]
        x.append(even)
    else:
        odd=a[i]
        y.append(odd)
    i=i+1
print("even=",x)
print("odd=",y)
