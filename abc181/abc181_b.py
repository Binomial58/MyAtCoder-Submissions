N=int(input())
S=0
for _ in range(N):
    a,b=map(int, input().split())
    S+=0.5*(b-a+1)*(a+b)
print(int(S))