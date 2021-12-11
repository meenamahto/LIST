# in first way-
places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
print(places[-1])
print(places[-2])
print(places[-3])
print(places[-4])
print(places[-5])
i=0
while i<len(places):
    rev=places[-i-1]
    i=i+1
    print(rev)

#second way-
places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
print(places[4])
print(places[3])
print(places[2])
print(places[1])
print(places[0])

#third way-
places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
i=0
while i<len(places):
  a=places[::-1]
  i=i+1
print(a)

#fourth way-
a=[1,2,3,4,5]
i=0
while i<len(a):
    a=a[::-1]
    i=i+1
print(a)

