import collections
N=int(input())
S=[]
R=[]
for i in range(N):
    s=input()
    S.append(s)
T=collections.Counter(S)
Y=T.most_common()
M=Y[0][1]
for i in range(len(Y)):
    if Y[i][1]==M:
        R.append(Y[i][0])
R.sort()
for r in R:
    print(r)