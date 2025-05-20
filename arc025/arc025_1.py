D=list(map(int, input().split()))
J=list(map(int, input().split()))
S=0
for i in range(7):
    S+=max(D[i],J[i])
print(S)