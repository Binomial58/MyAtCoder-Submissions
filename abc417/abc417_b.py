n,m=map(int, input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
C=[]
for a in set(A):
    s=max(A.count(a)-B.count(a),0)
    for u in range(s):
        C.append(a)
print(*C)