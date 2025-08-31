h,w=map(int, input().split())
S = [list(input()) for _ in range(h)]
T = [list(input()) for _ in range(h)]
S1=[[] for i in range(w)]
T1=[[] for i in range(w)]
S2=[]
T2=[]
for i in range(w):
    for j in range(h):
        S1[i].append(S[j][i])
        T1[i].append(T[j][i])
for i in range(w):
    S2.append("".join(S1[i]))
    T2.append("".join(T1[i]))
S2.sort()
T2.sort()
if S2==T2:
    print("Yes")
else:
    print("No")