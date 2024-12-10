A,B=map(int, input().split())
C=[1,1,1]
C[A-1]-=1
C[B-1]-=1
count=C.count(1)
if count==1:
    print(C.index(1)+1)
else:
    print("-1")