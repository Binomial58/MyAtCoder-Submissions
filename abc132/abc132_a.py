S=input()
T=[]
for i in range(4):
    if S[i]not in T:
        T.append(S[i])
if len(T)!=2:
    print("No")
else:
    if S.count(T[0])==2 and S.count(T[1])==2:
        print("Yes")