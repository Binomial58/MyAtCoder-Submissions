A=[list(map(int, input().split())) for i in range(3)]
N=int(input())
for i in range(N):
    x=int(input())
    for a in range(3):
        for b in range(3):
            if A[a][b]==x:
                A[a][b]="o"
for i in range(3):
    if A[i][0]==A[i][1]==A[i][2]:
        print("Yes")
        exit()
for i in range(3):
    if A[0][i]==A[1][i]==A[2][i]:
        print("Yes")
        exit()
if A[0][0]==A[1][1]==A[2][2] or A[0][2]==A[1][1]==A[2][0]:
        print("Yes")
        exit()
print("No")