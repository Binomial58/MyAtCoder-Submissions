N=int(input())
S,T=map(str, input().split())
U=""
for i in range(N):
    U+=S[i]
    U+=T[i]
print(U)