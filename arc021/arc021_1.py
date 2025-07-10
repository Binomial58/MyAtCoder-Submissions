A = [list(map(int, input().split())) for _ in range(4)]
for i in range(3):
    for j in range(4):
        if A[i][j]==A[i+1][j]:
            print("CONTINUE")
            exit()
#配列を転置する方法
A=list(zip(*A))
for i in range(3):
    for j in range(4):
        if A[i][j]==A[i+1][j]:
            print("CONTINUE")
            exit()
print("GAMEOVER")