N,K=map(int, input().split())
S=input()
M=""
for a in range(K-1):
    M+=S[a]
M+=S[K-1].lower()
for a in range(K,N):
    M+=S[a]
print(M)