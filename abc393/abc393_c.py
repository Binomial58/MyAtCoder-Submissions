N,M=map(int, input().split())
V=set()
c=0
for i in range(M):
    l=list(map(int, input().split()))
    l.sort()
    s=str(l[0])+":"+str(l[1])
    if l[0]==l[1]:
        c+=1
    else:
        if s in V:
            c+=1
        else:
            V.add(s)
print(c)
