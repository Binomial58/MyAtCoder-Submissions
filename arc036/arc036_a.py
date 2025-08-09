n,k=map(int, input().split())
T=[]
for i in range(n):
    T.append(int(input()))
s=0
sumT=[]
for t in T:
    s+=t
    sumT.append(s)
sumT2=[sumT[2]]
for i in range(n-3):
    sumT2.append(sumT[i+3]-sumT[i])
for i in range(n-2):
    if sumT2[i]<k:
        print(i+3)
        exit()
print(-1)