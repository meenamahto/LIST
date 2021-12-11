mylist = [[1,2,3],[4,5,6,7],[7,8,9],[8,9,10]]

# for x in mylist:
#       if len(x)==3:
#         print(x)


i=0
while i<len(mylist):
    if len(mylist[i])==4:
        print(mylist[i])
    i=i+1
