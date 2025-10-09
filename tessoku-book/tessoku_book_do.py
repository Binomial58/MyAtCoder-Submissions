n=int(input())
A=[]
B=[]
for i in range(n):
    a,b=map(int, input().split())
    A.append(a)
    B.append(b)
countm=0
# 表と裏が両方正
countA=0
countB=0
for i in range(n):
    if A[i]+B[i]>=0:
        countA+=A[i]
        countB+=B[i]
countm=max(countm,abs(countA)+abs(countB))
# 表が正
countA=0
countB=0
for i in range(n):
    if A[i]-B[i]>=0:
        countA+=A[i]
        countB+=B[i]
countm=max(countm,abs(countA)+abs(countB))
# 裏が正
countA=0
countB=0
for i in range(n):
    if -A[i]+B[i]>=0:
        countA+=A[i]
        countB+=B[i]
countm=max(countm,abs(countA)+abs(countB))
# 表と裏が両方正
countA=0
countB=0
for i in range(n):
    if -A[i]-B[i]>=0:
        countA+=A[i]
        countB+=B[i]
countm=max(countm,abs(countA)+abs(countB))
print(countm)