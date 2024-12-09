import math
#キョリ函数の導入
def dis(a,b,c,d):
    e=math.sqrt((a-c)**2+(b-d)**2)
    return e

N=int(input())
X=[0]
Y=[0]
s=0
for i in range(N):
    a,b=map(int,input().split())
    X.append(a)
    Y.append(b)
X.append(0)
Y.append(0)
for k in range(N+1):
    s+=dis(X[k],Y[k],X[k+1],Y[k+1])
print(s)