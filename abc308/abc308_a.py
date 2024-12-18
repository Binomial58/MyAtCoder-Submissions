S=list(map(int, input().split()))
for i in range(7):
    if S[i]>S[i+1] :
        print("No")
        exit()
for j in range(8):
    if S[j]<100 or S[j]>675 or S[j]%25!=0:
        print("No")
        exit()
print("Yes")