n=int(input())
t=0
count=0
L=[]
R=[]
for i in range(n):
    l,r=map(int, input().split())
    L.append(l)
    R.append(r)
R, L = zip(*sorted(zip(R, L)))
for i in range(n):
    if t<=L[i]:
        count+=1
        t=R[i]
print(count)