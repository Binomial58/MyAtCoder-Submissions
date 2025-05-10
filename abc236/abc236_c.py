N,M=map(int, input().split())
S=list(map(str, input().split()))
T=set(list(map(str, input().split())))
for i in range(N):
    if S[i]in T:
        print("Yes")
    else:
        print("No")