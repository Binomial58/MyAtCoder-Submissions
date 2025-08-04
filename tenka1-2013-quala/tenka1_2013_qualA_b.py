n=int(input())
c=0
for i in range(n):
    R=list(map(int, input().split()))
    if 0<=sum(R)<20:
        c+=1
print(c)