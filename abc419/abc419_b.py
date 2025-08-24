q=int(input())
T=[]
R=[]
for i in range(q):
    l=list(map(str, input().split()))
    if l[0]=="1":
        T.append(int(l[1]))
        T.sort()
    else:
        R.append(T[0])
        T.pop(0)
for r in R:
    print(r)