Q=int(input())
C=[0]*100
B=[]
for i in range(Q):
    a,*b=map(int, input().split())
    if a==2:
        B.append(C[-1])
        C.pop()
    else:
        C.append(*b)
for i in range(len(B)):
    print(B[i])