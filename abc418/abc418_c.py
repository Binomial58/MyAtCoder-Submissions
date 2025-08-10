n,q=map(int, input().split())
A=list(map(int, input().split()))
A.sort()
B=set(A)
countA={}
for a in A:
    if a not in countA:
        countA[a]=1
    else:
        countA[a]+=1
R=[]
S=[]
s=-(n-1)
c=n
for i in range(1,max(A)+1):
    s+=c
    S.append(s)
    if i-1 in B:
        c-=countA[i-1]
m=max(A)
for i in range(q):
    s=0
    b=int(input())
    if b>m:
        R.append(-1)
    else:
        R.append(S[b-1])
for r in R:
    print(r)
