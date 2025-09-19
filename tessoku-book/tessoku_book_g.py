d=int(input())
n=int(input())
N=[0 for i in range(d+1)]
for i in range(n):
    l,r=map(int, input().split())
    N[l-1]+=1
    N[r]-=1
Nsum=[N[0]]
for i in range(d-1):
    Nsum.append(Nsum[i]+N[i+1])
for j in Nsum:
    print(j)
