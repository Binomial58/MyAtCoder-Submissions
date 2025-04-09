S=input()
T=[]
for i in range(len(S)):
    T.append(S[i])
T.sort()
R=""
for j in range(len(S)):
    R+=T[j]
print(R)