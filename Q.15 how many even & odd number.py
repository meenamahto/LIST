a=[]
s=int(input("Enter your number of size:"))
b=1
while b<=s:
    n=int(input("Enter your number:"))
    a.append(n)
    b=b+1
i=0
even=0
odd=0
while i<len(a):
    if a[i]%2==0:
        even=even+1
    else:
        odd=odd+1
    i=i+1
print("even=",even)
print("odd=",odd)

