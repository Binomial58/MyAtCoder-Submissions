N=int(input())
A=[]
B=[]
for i in range(N):
    a,b=map(int, input().split())
    A.append(a)    
    B.append(b)
if A.index(min(A))!=B.index(min(B)):
    print(max(min(A),min(B)))
else:
    B.sort()
    if min(A)+min(B)<=max(min(A),B[1]):
        print(min(A)+min(B))
    else:
        print(max(min(A),B[1]))