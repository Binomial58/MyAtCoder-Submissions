n=int(input())
A=list(map(int, input().split()))
d=int(input())
Bleft=[0 for i in range(n+2)]
Bright=[0 for i in range(n+2)]
R=[]
for i in range(n):
    Bleft[i+1]=max(Bleft[i],A[i])
    Bright[n-i]=max(Bright[n-i+1],A[n-i-1])
for i in range(d):
    l,r=map(int, input().split())
    R.append(max(Bleft[l-1],Bright[r+1]))
for r in R:
    print(r)