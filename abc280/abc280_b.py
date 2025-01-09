N=int(input())
S=list(map(int, input().split()))
B=[]
b=0
for i in range(N):
    B.append(S[i]-b)
    b+=S[i]-b
print(*B)