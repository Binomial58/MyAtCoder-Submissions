N=int(input())
K=int(input())
L=1
for i in range(N):
    if L*2>=L+K:
        L+=K
    else:
        L*=2
print(L)