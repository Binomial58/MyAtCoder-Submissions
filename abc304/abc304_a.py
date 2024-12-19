N=int(input())
S=[]
A=[]
B=[i for i in range(N)]
for _ in range(N):
    s,a=input().split()
    a=int(a)
    S.append(s)
    A.append(a)
i=A.index(min(A))
B=[(b-i)%N for b in B]
B,S=zip(*sorted(zip(B,S)))
for s in S:
    print(s)  