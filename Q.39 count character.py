list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
c=0
c1=0
c2=0
c3=0
while i<len(list):
    if list[i]=="a":
        c=c+1
    if list[i]=="n":
        c1=c1+1
    if list [i]=="t":
        c2=c2+1
    if list[i]=="x":
        c3=c3+1
    i=i+1
b=[["a",c],["n",c1],["t",c2],["x",c3]]
print(b)

