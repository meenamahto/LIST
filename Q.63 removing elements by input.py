a=[1, 1, 2, 3, 4, 5, 1, 2]
n=int(input("Enter your number:"))
i=0
b=[]
while i<len(a):
    if a[i]!=n:
        b.append(a[i])
    i=i+1
print(b)
