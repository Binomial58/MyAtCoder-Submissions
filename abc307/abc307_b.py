N=int(input())
S=[input() for _ in range(N)]
for i in range(N):
    for j in range(N):
        d=""
        if i!=j:
            d=S[i]+S[j]
            l=len(d)
            if all(d[p]==d[l-p-1] for p in range(l)):
                print("Yes")
                exit()
print("No")