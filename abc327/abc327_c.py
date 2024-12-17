A=[list(map(int, input().split())) for _ in range(9)]
for i in range(9):
    if len({A[k][i] for k in range(9)}) !=9:
        print("No")
        exit()
for k in range(9):
    if len({A[k][i] for i in range(9)}) !=9:
        print("No")
        exit()
for a in range(0,9,3):
    for b in range(0,9,3):
        if len({A[a+C][b+D] for C in range(3) for D in range(3)}) !=9:
            print("No")
            exit()
print("Yes")