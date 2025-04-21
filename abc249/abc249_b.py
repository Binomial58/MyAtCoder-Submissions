S=input()
A=0
a=0
for i in range(len(S)):
    if S[i].isupper():
        A+=1
    if S[i].islower():
        a+=1
if A==len(S) or a==len(S):
    print("No")
else:
    if len(S)==len(set(S)):
        print("Yes")
    else:
        print("No")