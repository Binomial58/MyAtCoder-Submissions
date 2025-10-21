n,m=map(int, input().split())
B=list(map(int, input().split()))
W=list(map(int, input().split()))
B.sort(reverse=True)
W.sort(reverse=True)
ob=len(B)
s=0
if len(B)>len(W):
    W+=[0 for i in range(len(B)-len(W))]
else:
    B+=[0 for i in range(len(W)-len(B))]
j=len(W)
for i in range(ob):
    if B[i]>=0:
        s+=B[i]
    else:
        j=i
        break
# print(s)
u=True
for k in range(min(j,ob)):
    if W[k]>=0:
        s+=W[k]
    else:
        u=False
        break
# print(s)
if u:
    for t in range(j,ob):
        if W[t]+B[t]>=0:
            s+=W[t]+B[t]
        else:
            break
print(s)