N,M=map(int, input().split())
D=[[]for i in range(N)]
for j in range(M):
    a,b=map(int, input().split())
    D[a-1].append(b)
    D[b-1].append(a)
for d in D:
    d.sort()
    print(len(d),*d)