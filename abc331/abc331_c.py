n=int(input())
A=list(map(int, input().split()))
B=list(set(A))
B.sort()
R=[]
countA={}
for a in A:
    if a not in countA:
        countA[a]=1
    else:
        countA[a]+=1
sumA={}
s=sum(A)
c=0
for b in B:
    c+=b*countA[b]
    sumA[b]=c
for a in A:
    R.append(s-sumA[a])
print(*R)