A=list(map(int, input().split()))
d=0
for i in range(64):
    d+=A[i]*2**i
print(d)