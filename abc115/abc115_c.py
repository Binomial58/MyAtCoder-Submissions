from collections import Counter
import bisect
n,k=map(int, input().split())
H=[]
for i in range(n):
    H.append(int(input()))
C=Counter(H)
Element=list(set(H))
Element.sort()
P=[]
for e in Element:
    P.append(C[e])
sumP=[P[0]] 
for i in range(len(Element)-1):
    sumP.append(sumP[i]+P[i+1])
sumP.append(10**9)
R=[]
for i in range(len(Element)):
    if i!=0:
        j=bisect.bisect_left(sumP,k+sumP[i-1])
    else:
        j=bisect.bisect_left(sumP,k)
    if j<len(Element):
        R.append(Element[j]-Element[i])
print(min(R))