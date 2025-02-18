S=input()
a,b=map(int, input().split())
M=""
for i in range(a-1):
    M+=S[i]
M+=S[b-1]
for k in range(a,b-1):
    M+=S[k]
M+=S[a-1]
for j in range(b,len(S)):
    M+=S[j]
print(M)