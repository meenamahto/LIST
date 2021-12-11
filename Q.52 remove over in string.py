mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
subStr = "over"

a=mainStr.split()
n=input("enter your word:")
for i in a:
    if i==n:
        a.remove(n)
mainStr=' '.join(a)
print(mainStr)

print(mainStr.replace("over","on"))


# replace on using function-

a=mainStr.replace(subStr,"on")
print(a)