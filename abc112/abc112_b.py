N,T=map(int, input().split())
m=10**10
for i in range(N):
    c,t=map(int, input().split())
    if t<=T:
        m=min(m,c)
if m==10**10:
    print("TLE")
else:
    print(m)