N=int(input())
C=[]
for _ in range(N):
    a,b=map(int, input().split())
    C.append(a+b)
for i in range(N):
    print(C[i])