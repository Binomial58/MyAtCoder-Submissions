n,m=map(int, input().split())
A=list(map(int, input().split()))
Num={}
win=0
num=10*10
for a in A:
    if a not in Num:
        Num[a]=1
    else:
        Num[a]+=1
    if win<Num[a]:
        print(a)
        win=Num[a]
        num=a
    elif win==Num[a]:
        if num>a:
            print(a)
            win=Num[a]
            num=a
        else:
            print(num)
    else:
        print(num)