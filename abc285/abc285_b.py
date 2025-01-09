N=int(input())
S=input()
for i in range(1,N):
    a=0
    for k in range(N-i):
        if S[k]!=S[k+i]:
            a+=1
        elif S[k]==S[k+i]:
            break
    print(a)