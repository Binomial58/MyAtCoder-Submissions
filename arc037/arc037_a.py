N=int(input())
M=list(map(int, input().split()))
S=0
for m in M:
    if m<80:
        S+=80-m
print(S)