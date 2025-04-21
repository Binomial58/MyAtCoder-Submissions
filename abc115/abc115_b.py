N=int(input())
P=[]
for _ in range(N):
    p=int(input())
    P.append(p)
print(sum(P)-(max(P)//2))