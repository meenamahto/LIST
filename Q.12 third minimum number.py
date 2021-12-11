numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
min=numbers[i]
while i<len(numbers):
    if numbers[i]<min:
        min=numbers[i]
    i=i+1
print(min)
i=0
min1=numbers[i]
while i<len(numbers):
    if numbers[i]<min1:
        if numbers[i] != min:
            min1=numbers[i]
    i=i+1
print(min1)
i=0
min2=numbers[i]
while i<len(numbers):
    if numbers[i]<min2:
        if numbers[i]!=min and numbers[i]!=min1:
            min2=numbers[i]
    i=i+1
print(min2)
