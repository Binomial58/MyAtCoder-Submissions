from collections import defaultdict
N=int(input())
A=[]
C=[]
#最小値の最大値の初期化
Min=0
for _ in range(N):
    a,c=map(int, input().split())
    A.append(a)
    C.append(c)
D=defaultdict(list)
#豆の色ごとにおいしさの値を格納
for c,a in zip(C,A):
    D[c].append(a)
#おいしさの最小値の最大値を更新
for k in D:
    Min=max(Min,min(D[k]))
print(Min)