K,N=map(int, input().split())
A=list(map(int, input().split()))
B=A+[A[0]]
m=10**10
for i in range(N):
    d=max(K-abs(B[i]-B[i+1]),abs(B[i]-B[i+1]))
    m=min(m,d)
print(m)