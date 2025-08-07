n=int(input())
A=list(map(int, input().split()))
c=0
for a in A:
    while True:
        if a%2==0 or a%3==2:
            a-=1
            c+=1
        else:
            break
print(c)