# a="meena"
# i=0
# c=5
# b=[]
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         b.append([a[i][j],c])
#         c=c+5
#         j+=1
#     i=i+1
# print(b)


s=(input("Enter your number:"))
s1=""
i=0
for x in s:
    if s.index(x)==i:
        s1=s1+x
    i=i+1
print(s1)

