n = [50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
max=0
while i<len(n):
    if n[i]>max:
        max=n[i]
    i=i+1
# print(max)
i=0
max1=0
while i<len(n):
    if n[i]>max1:
        if n[i]!=max:
            max1=n[i]
    i=i+1
print(max1)
