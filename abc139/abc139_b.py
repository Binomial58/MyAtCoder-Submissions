A,B=map(int, input().split())
k=1
c=0
while k<B:
    k+=A-1
    c+=1
print(c)