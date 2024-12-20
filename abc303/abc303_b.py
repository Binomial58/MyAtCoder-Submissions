import math
N,M=map(int, input().split())
A=[list(map(int, input().split()))for _ in range(M)]
B=[]
for i in range(M):
    for k in range(N-1):
        if A[i][k]>A[i][k+1]:
            B.append(str(A[i][k+1])+str(A[i][k]))
        else:
            B.append(str(A[i][k])+str(A[i][k+1]))
B=set(B)
print(math.comb(N,2)-len(B))#組み合わせの総数を出す関数