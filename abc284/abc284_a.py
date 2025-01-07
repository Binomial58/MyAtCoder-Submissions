N=int(input())
S=[]
for _ in range(N):
    s=input()
    S.append(s)
for i in range(N):
    print(S[N-1-i])