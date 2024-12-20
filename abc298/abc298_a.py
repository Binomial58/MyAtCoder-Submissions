N=int(input())
S=input()
b=S.count("x")
g=S.count("o")
if b!=0 or g==0:
    print("No")
else:
    print("Yes")