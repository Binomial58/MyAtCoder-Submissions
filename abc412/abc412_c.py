import bisect
T=int(input())
R=[]
for i in range(T):
    N=int(input())
    S=list(map(int, input().split()))
    c=2
    a=S[0]
    b=S[-1]
    L=S[1:N-1]
    L.sort()
    r=0
    for j in range(len(L)):
        if a*2>=b:
            R.append(c)
            r=1
            break
        else:
            d=bisect.bisect(L,a*2)
            if a*2<L[d-1]:
                break
            a=L[d-1]
            c+=1
    if a*2<b:
        R.append(-1)
    elif r==0:
        R.append(c)
for r in R:
    print(r)