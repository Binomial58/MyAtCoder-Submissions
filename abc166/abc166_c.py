n,m=map(int, input().split())
H=list(map(int, input().split()))
E=[set() for i in range(n)]
done=set()
for i in range(m):
    a,b=map(int, input().split())
    E[a-1].add(b-1) 
    E[b-1].add(a-1) 
c=0
for i in range(n):
    flag=True
    if i not in done:
        for j in E[i]:
            if H[i]<=H[j]:
                flag=False
                break
        if flag:
            c+=1
            done.add(i)
print(c) 