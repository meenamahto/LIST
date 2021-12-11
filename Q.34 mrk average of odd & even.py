elt = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
count=0
count1=0
even=0
odd=0
while i<len(elt):
    if elt[i]%2==0:
        count=count+1
        even=even+elt[i]
    else:
        count1=count1+1
        odd=odd+elt[i]
    i=i+1
print("average of even=",even//count)
print("average of odd=",odd//count1)
