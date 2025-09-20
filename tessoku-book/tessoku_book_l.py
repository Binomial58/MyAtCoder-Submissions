import math
def Printer(A,j):
    count=0
    for a in A:
        count+=math.floor(j/a)
    return count
n,k=map(int, input().split())
A=list(map(int, input().split()))
A.sort()
l=1
r=10**9
i=(r+l)//2
while r!=l:
    if Printer(A,i)>=k:
        r=i
        i=(r+l)//2
    elif Printer(A,i)<k:
        l=i+1
        i=(r+l)//2
print(i)