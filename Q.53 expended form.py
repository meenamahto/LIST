# 2 digit code-
s=int(input("Enter your number of size:"))
a=[]
b=1
while b<=s:
    n=int(input("Enter your number:"))
    a.append(n)
    b=b+1
print(a)
a=[12,34,56,67]
i=0
rem=0
sum=0
while i<len(a):
    rem=a[i]%10
    sum=a[i]//10
    sum=sum*10
    i=i+1
    print(sum,"+",rem)
    


# 4 digit code-

s=int(input("Enter your number:"))
b=1
i=0
a=[]
while b<=s:
    n=int(input("Enter your number:"))
    a.append(n)
    b=b+1
print(a)
i=0
while i<len(a):
    rem=(a[i]//100)%10
    c=a[i]//1000
    sum=c*1000
    c1=rem*100
    rem1=a[i]//10%10
    c2=a[i]//100
    sum1=c2*100
    c3=rem1*10
    rem2=a[i]%10
    i=i+1
    print(sum,"+",c1,"+",c3,"+",rem2)


#5 digit code-
s=int(input("Enter your number:"))
b=1
i=0
a=[]
while b<=s:
    n=int(input("Enter your number:"))
    a.append(n)
    b=b+1
print(a)
i=0
while i<len(a):
    rem=(a[i]//1000)%10
    c=a[i]//10000
    sum=c*10000
    c1=rem*1000
    rem1=a[i]//100%10
    c2=a[i]//1000
    sum1=c2*1000
    c3=rem1*100
    rem2=a[i]//10%10
    c4=a[i]//100
    c5=rem2*10
    sum2=c4*100
    rem3=a[i]%10
    i=i+1
    # print(sum,"+",c1,"+",c3,"+","+",c5,"+",rem3)
    print(sum,"+",c3,"+",rem3)


#all digit code-
a=input("Enter your number:")
b=""
i=0
while i<len(a):
    b+=a[i]
    j=1
    while j<=len(a)-(i+1):
        b+="0"
        j=j+1
    if i==(len(a)-1):
        break
    else:
        b+="+"
    i=i+1
print(b)