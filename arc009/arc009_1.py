N=int(input())
S=0
for i in range(N):
    a,b=map(int, input().split())
    S+=a*b
print(int(S*1.05//1))