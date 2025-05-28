N=int(input())
S=input()
if S[0]!=S[N-1]:
    print(1)
else:
    for i in range(1,N-1):
        if S[0]!=S[i] and S[0]!=S[i+1]:
            print(2)
            exit()
    print(-1)