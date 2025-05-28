N=int(input())
A=list(map(int, input().split()))
A.sort(reverse=True)
E=[]
O=[]
e=0
o=0
for i in range(N):
    if A[i]%2==0:
        E.append(A[i])
        e+=1
    else:
        O.append(A[i])
        o+=1
    if e==2 and o==2:
        break
if e<2 and o <2:
    print(-1)
elif e>=2 and o<2:
    print(E[0]+E[1])
elif e<2 and o>=2:
    print(O[0]+O[1])
else:
    print(max(E[0]+E[1],O[0]+O[1]))
    