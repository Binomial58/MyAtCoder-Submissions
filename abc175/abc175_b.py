N=int(input())
L=list(map(int, input().split()))
C=0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if i==j or j==k or k==i:
                break
            D=[L[i],L[j],L[k]]
            D.sort()
            if D[0]+D[1]>D[2] and len(set(D))==3:
                C+=1
print(C)