N,M=map(int, input().split())
S=[input() for _ in range(N)]
T=[input() for _ in range(M)]
count=0
for i in range(N):
    s=S[i][-3]+S[i][-2]+S[i][-1]
    if T.count(s)>0:
        count+=1
print(count)