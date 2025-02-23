N=int(input())
A=list(map(int, input().split()))
S=0
for a in A:
    if a>=10:
        S+=a-10
print(S)