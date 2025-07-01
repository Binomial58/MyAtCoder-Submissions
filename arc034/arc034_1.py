N=int(input())
m=0
for i in range(N):
    a,b,c,d,e=map(int, input().split())
    e=e*(110/900)
    m=max(m,a+b+c+d+e)
print(m)