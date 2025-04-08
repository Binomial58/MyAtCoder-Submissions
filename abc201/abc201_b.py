N=int(input())
S=[]
T=[]
for _ in range(N):
    s,t=map(str, input().split())
    S.append(s)
    T.append(int(t))
T,S=zip(*sorted(zip(T,S)))
print(S[N-2])