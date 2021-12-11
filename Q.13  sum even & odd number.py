a=[]
s=int(input("Enter your number of size:"))
b=1
while b<=s:
    n=int(input("Enter your number:"))
    a.append(n)
    b=b+1
even=0
odd=0
i=0
while i<len(a):
    if a[i]%2==0:
        even=even+a[i]
    else:
        odd=odd+a[i]
    i=i+1
print("odd=",odd,"even=",even)