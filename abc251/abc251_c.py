n=int(input())
P=[]
S=set()
for i in range(n):
    s,t=map(str, input().split())
    t=int(t)
    if s not in S:
        S.add(s)
        P.append([t,i+1])
P.sort(key=lambda x: (-x[0], x[1]))
print(P[0][1])