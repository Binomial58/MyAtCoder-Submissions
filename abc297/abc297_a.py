N,D=map(int, input().split())
T=list(map(int, input().split()))
for n in range(N-1):
    if T[n+1]-T[n]<=D:
        print(T[n+1])
        exit()
print("-1")