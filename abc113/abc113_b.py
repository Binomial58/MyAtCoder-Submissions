N=int(input())
T,A=map(int, input().split())
H=list(map(int, input().split()))
R=[]
for i in range(N):
    R.append(abs(T-H[i]*0.006-A))
print(R.index(min(R))+1)