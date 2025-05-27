N,K=map(int, input().split())
print(min(abs(N-K*(N//K)),abs(N-K*((N//K)+1))))