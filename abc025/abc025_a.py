S=input()
N=int(input())
D=[]
for i in range(len(S)):
    for j in range(len(S)):
        d=S[i]+S[j]
        D.append(d)
D.sort()
print(D[N-1])