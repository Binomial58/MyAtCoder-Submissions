C = [list(map(int, input().split())) for i in range(3)]
# print(C)
for i in range(3):
    if not (
        C[i][0] - C[(i + 1) % 3][0]
        == C[i][1] - C[(i + 1) % 3][1]
        == C[i][2] - C[(i + 1) % 3][2]
    ):
        print("No")
        exit()
    if not (
        C[0][i] - C[0][(i + 1) % 3]
        == C[1][i] - C[1][(i + 1) % 3]
        == C[2][i] - C[2][(i + 1) % 3]
    ):
        print("No")
        exit()
print("Yes")
