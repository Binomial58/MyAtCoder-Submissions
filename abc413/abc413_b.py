N=int(input())
S=[]
T=set()
for s in range(N):
    s=input()
    S.append(s)
for i in range(N):
    for j in range(N):
        if i!=j:
            T.add(S[i]+S[j])
print(len(T))