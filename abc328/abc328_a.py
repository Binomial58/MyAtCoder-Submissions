N,X=map(int, input().split())
S=list(map(int, input().split()))
R=0
for s in S:
    if s<=X:
        R+=s
print(R)