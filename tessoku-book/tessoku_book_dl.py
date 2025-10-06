n,d=map(int, input().split())
Y=[[] for i in range(d)]
C=[]
count=0
for i in range(n):
    x,y=map(int, input().split())
    Y[x-1].append(y)
for i in range(d):
    for j in Y[i]:
        C.append(j)
    C.sort()
    if len(C)!=0:
        count+=C.pop(-1)
print(count)