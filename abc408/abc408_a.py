N,S=map(int, input().split())
T=[0]+list(map(int, input().split()))
t=S
for i in range(1,N+1):
    t-=T[i]-T[i-1]
    if t<0:
        print("No")
        exit()
    else:
        t=S
print("Yes")