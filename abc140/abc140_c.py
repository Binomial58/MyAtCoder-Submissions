N=int(input())
B=list(map(int, input().split()))
S=B[-1]+B[0]
for i in range(N-2):
    S+=min(B[i],B[i+1])
print(S)