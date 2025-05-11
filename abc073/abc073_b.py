N=int(input())
S=0
for i in range(N):
    l,r=map(int, input().split())
    S+=r-l+1
print(S)