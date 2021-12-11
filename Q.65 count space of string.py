a="the quick brown fox jumped over the lazy dog. the dog slept over the verandah"
i=0
count=0
while i<len(a):
    if a[i]==" ":
        count=count+1
    i=i+1
print(count)