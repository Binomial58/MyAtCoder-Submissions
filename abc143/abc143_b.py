N=int(input())
d=list(map(int, input().split()))
S=0
for i in range(N):
    for j in range(N):
        if i==j:
            break
        S+=d[i]*d[j]
print(S)