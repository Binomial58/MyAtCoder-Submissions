N=int(input())
c=0
for i in range(N):
    a,b=map(int, input().split())
    if b>a:
        c+=1
print(c)