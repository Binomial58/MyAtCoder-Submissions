N=int(input())
S=0
D=0
for _ in range(N):
    s=input()
    if s=="login":
        D=1
    elif s=="logout":
        D=0
    elif s=="private" and D==0:
        S+=1
print(S)