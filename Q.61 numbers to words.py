num = int(input("Enter any number:"))
t = []
while num > 0:
    rem = num %10
    if rem == 0:
        t.append("Zero")
    elif rem == 1:
        t.append("One")
    elif rem == 2:
        t.append("Two")
    elif rem == 3:
        t.append("Three")
    elif rem == 4:
        t.append("Four")
    elif rem == 5:
        t.append("Five")
    elif rem == 6:
        t.append("Six")
    elif rem == 7:
        t.append("Seven")
    elif rem == 8:
        t.append("Eight")
    elif rem == 9:
        t.append("Nine")
    num = num // 10
for i in range(len(t)-1,-1,-1):
    print(t[i],end=" ")