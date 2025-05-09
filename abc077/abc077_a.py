A=input()
B=input()
if A==B[::-1] and B==A[::-1]:
    print("YES")
else:
    print("NO")