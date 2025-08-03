import collections
n=int(input())
A=list(map(int, input().split()))
J=[]
I=[]
c=0
for j in range(1,n+1):
    J.append(j-A[j-1])
    I.append(j+A[j-1])
J2=collections.Counter(J)
I2=collections.Counter(I)
K=set(J)&set(I)
for k in K:
    c+=J2[k]*I2[k]
print(c)