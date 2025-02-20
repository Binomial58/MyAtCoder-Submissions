N=int(input())
S=0
if N%100==0:
    S-=1
print(S+N//100+1)