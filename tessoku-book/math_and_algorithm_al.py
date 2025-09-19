t=int(input())
n=int(input())
B=[0 for i in range(t+1)]
for i in range(n):
    l,r=map(int, input().split())
    B[l]+=1
    B[r]-=1
Bsum=[B[0]]
for i in range(t):
    Bsum.append(Bsum[i]+B[i+1])
for b in range(t):
    print(Bsum[b])