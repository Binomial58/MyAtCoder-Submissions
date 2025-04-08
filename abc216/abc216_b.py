N=int(input())
S,T=[],[]
for _ in range(N):
    s,t=map(str, input().split())
    S.append(s)
    T.append(t)
for a in range(N):
    for b in range(N):
        if a==b:
            break
        if S[a]==S[b] and T[a]==T[b]:
            print("Yes")
            exit()
print("No")