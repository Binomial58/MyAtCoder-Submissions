N=int(input())
A=list(map(int, input().split()))
S=0
for a in A:
    S+=a-1
print(S)