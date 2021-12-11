n=[50, 39, 23, 70, 56, 12, 5, 30, 7]
i=0
count=0
while i<len(n):
    if n[i]>20 and n[i]<40:
        count=count+1
    i=i+1
print(count)