N=int(input())
A=list(map(int, input().split()))
R=[]
L=0
for i in range(N):
    R.append(A[i])
    L+=1
    if L>=2:
        while True:
            if R[L-1]==R[L-2]:
                D=R[L-1]
                R.pop(-1)
                R.pop(-1)
                R.append(D+1)
                L-=1
            else:
                break
            if L==1:
                break
print(L)