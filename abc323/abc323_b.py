N=int(input())
S=[]
for k in range(1,N+1):
    s=input()
    t=s.count("o")
    S.append([k,t])
#得点が高い順にソート，得点が同じ場合は名前が小さい方を前にソート
S.sort(key=lambda x:(-x[1],x[0]))
T=[S[i][0] for i in range(N)]
print(*T)