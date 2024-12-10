N,M=map(int, input().split())
H=list(map(int, input().split()))
d=0
for i in range(N):
    M-=H[i]
    if M >=0:
        d+=1
print(d)