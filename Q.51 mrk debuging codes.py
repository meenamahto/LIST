name = ["Savitri", "Phule", "26"]
print (name[0]+name[1])


marks = ["10", "32", "42", "65", "67", "89", "76", "38", "67"]
total_marks = 0
counter = 0
while counter < len(marks):
    j=0
    while j<len(marks):
        c=int(marks[counter])
        total_marks = total_marks + c
        j=j+1
    counter = counter + 1
print(total_marks)