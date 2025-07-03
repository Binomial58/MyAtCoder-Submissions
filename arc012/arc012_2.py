N,a,b,L=map(int, input().split())
A=0
B=L
for i in range(N):
    t=L/a
    A+=a*t
    B+=b*t
    L=B-A
print(L)