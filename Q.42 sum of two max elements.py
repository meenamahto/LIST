a=[12,2,3,-3,43,-23,-11,44]
# # a.sort(reverse=True)

i=0
max=0
while i<len(a):
    if a[i]>max:
        max=a[i]
    i=i+1
i=0
max1=0
while i<len(a):
    if a[i]>max1:
        if a[i]!=max:

            max1=a[i]
    i=i+1
print(max+max1)
