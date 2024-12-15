S=input()
L=len(S)
if S[0]!=S[1] and S[1]==S[2]:
    print(1)
    exit()
for k in range(1,L-1):
    if S[k-1]!=S[k] and S[k]!=S[k+1]:
        print(k+1)
        exit()
print(L)