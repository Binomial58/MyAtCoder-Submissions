S=input()
T=input()
B=[]
for i in range(1,len(S)):
    if S[i].isupper():
        B.append(S[i-1])
for b in B:
    if b not in T:
        print("No")
        exit()
print("Yes")