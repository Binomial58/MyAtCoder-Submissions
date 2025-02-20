N,M=map(int, input().split())
A=list(map(int, input().split()))
B=[i for i in range(1,N+1)]
A=set(A)
B=set(B)
C=list(B-A)
print(len(C))
C.sort()
print(*C)