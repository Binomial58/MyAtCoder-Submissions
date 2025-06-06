N=int(input())
S=input()
C=0
t=1
for i in range(N-1):
    if S[i]==">":
        t+=1
    else:
        C+=t*(t-1)//2
        t=1
C+=t*(t-1)//2
print(C)