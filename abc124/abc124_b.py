N=int(input())
H=list(map(int, input().split()))
M=H[0]
C=1
for i in range(1,N):
    if M<=H[i]:
        C+=1
        M=H[i]
print(C)