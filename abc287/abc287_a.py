N=int(input())
#1番目がFor
T=[0]*2
for _ in range(N):
    S=input()
    if S=="For":
        T[0]+=1
    else:
        T[1]+=1
if T[0]>T[1]:
    print("Yes")
else:
    print("No")