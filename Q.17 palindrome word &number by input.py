n=input("Enetr your name:")
i=0
rev=n[-1::-1]
while i<len(n):
    if rev==n:
        print("palindrome number",rev)
        break
    else:
        print("not palindrome number",rev)
        break
