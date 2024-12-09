N=int(input())
A=list(map(int,input().split()))
T=[]
for i in range(N):
    T.append(i+1)
A,T=zip(*sorted(zip(A,T)))
print(T[N-2])