n,k=map(int, input().split())
s=input()
C=[set() for i in range(n+100)]
for i in range(n-k+1):
    t=s[i:i+k]
    count=0
    for j in range(n-k+1):
        if t==s[j:j+k]:
            count+=1
    C[count].add(t)
maxi=0
for i in range(n+100):
    if len(C[i])!=0:
        maxi=i
print(maxi)
R=list(C[maxi])
R.sort()
print(*R)