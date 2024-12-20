N=int(input())
S=input()
if N==1:
    print("Yes")
    exit()
for i in range(N-1):
    if S[i]==S[i+1]:
        print("No")
        exit()
print("Yes")