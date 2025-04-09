N,D=map(int, input().split())
S=0
for _ in range(N):
    x,y=map(int, input().split())
    if x**2+y**2<=D**2:
        S+=1
print(S)