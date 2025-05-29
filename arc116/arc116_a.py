N=int(input())
T=[]
for i in range(N):
    t=int(input())
    if t%2!=0:
        T.append("Odd")
    else:
        if t%4==0:
            T.append("Even")
        else:
            T.append("Same")
for r in T:
    print(r)