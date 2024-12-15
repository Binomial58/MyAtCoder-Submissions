from collections import defaultdict

S=input()
P=[i for i in range(len(S))]
D=defaultdict(list)
for s,p in zip(S,P):
    D[s].append(p)
E=sorted(D.items())
if len(E)==1:
    print("Yes")
    exit()
for k in range(len(E)-1):
    if max(E[k][1])>min(E[k+1][1]):
        print("No")
        exit()
print("Yes")