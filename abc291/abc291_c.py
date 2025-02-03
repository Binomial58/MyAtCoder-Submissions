import collections
N=int(input())
S=input()
T=[(0,0)]
for i in range(N):
    if S[i]=="R":
        T.append((T[i][0]+1,T[i][1]))
    if S[i]=="L":
        T.append((T[i][0]-1,T[i][1]))
    if S[i]=="U":
        T.append((T[i][0],T[i][1]+1))
    if S[i]=="D":
        T.append((T[i][0],T[i][1]-1))
U=collections.Counter(T)
Y=U.most_common()
if Y[0][1]!=1:
    print("Yes")
else:
    print("No")