N,K,Q=map(int, input().split())
P=[0]*N
B=[K]*N
for i in range(Q):
    A=int(input())
    P[A-1]+=1
for i in range(N):
    B[i]-=Q-P[i]
for b in B:
    if b<=0:
        print("No")
    else:
        print("Yes")