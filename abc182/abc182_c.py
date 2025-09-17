n=input()
A=[]
for i in range(len(n)):
    A.append(int(n[i])%3)
S=sum(A)
if S%3==2:
    if 2 in A and len(n)>1:
        print(1)
    elif A.count(1)>=2 and len(n)>2:
        print(2)
    else:
        print(-1)
elif S%3==1:
    if 1 in A and len(n)>1:
        print(1)
    elif A.count(2)>=2 and len(n)>2:
        print(2)
    else:
        print(-1)
else:
    print(0)