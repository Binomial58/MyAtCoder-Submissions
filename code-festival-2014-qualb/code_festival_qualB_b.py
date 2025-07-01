N,K=map(int, input().split())
C=0
A=[]
for i in range(N):
    a=int(input())
    A.append(a)
for i in range(N):
    C+=A[i]
    if C>=K:
        print(i+1)
        exit()