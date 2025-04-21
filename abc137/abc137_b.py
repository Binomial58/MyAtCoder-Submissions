K,X=map(int, input().split())
A=X-K+1
C=[]
for i in range(K*2-1):
    C.append(A+i)
print(*C)