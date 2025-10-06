n=int(input())
s=input()
G=[1 for i in range(n)]
for i in range(n-1):
    if s[i]=="A":
        G[i+1]=G[i]+1
for j in range(n-1,0,-1):
    if s[j-1]=="B" and G[j]>=G[j-1]:
        G[j-1]=G[j]+1
print(sum(G))