N=int(input())
D=[]
S=1
for i in range(N):
    d=int(input())
    D.append(d)
D.sort(reverse=True)
for i in range(1,N):
    if D[i-1]==D[i]:
        continue
    S+=1
print(S)