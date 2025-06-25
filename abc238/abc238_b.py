N=int(input())
A=list(map(int, input().split()))
C=0
B=[0]
for a in A:
    C+=a
    B.append(C%360)
B.sort()
B.append(360)
m=0
for i in range(N+1):
    m=max(m,B[i+1]-B[i])
print(m)