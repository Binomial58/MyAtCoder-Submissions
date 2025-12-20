h, w = map(int, input().split())
C = (
    [["." for i in range(w)]]
    + [list(input()) for _ in range(h)]
    + [["." for i in range(w)]]
)
for i in range(h + 2):
    C[i] = ["."] + C[i] + ["."]
R = [0 for i in range(min(h, w))]
for a in range(1, 1 + h):
    for b in range(1, 1 + w):
        lu = [a, b]
        ru = [a, b]
        ld = [a, b]
        rd = [a, b]
        for k in range(len(R)):
            if C[a][b] == "#":
                lu = [lu[0] - 1, lu[1] - 1]
                ru = [ru[0] - 1, ru[1] + 1]
                ld = [ld[0] + 1, ld[1] - 1]
                rd = [rd[0] + 1, rd[1] + 1]
                if (
                    C[lu[0]][lu[1]] == "#"
                    and C[ru[0]][ru[1]] == "#"
                    and C[ld[0]][ld[1]] == "#"
                    and C[rd[0]][rd[1]] == "#"
                ):
                    R[k] += 1
                    if k != 0:
                        R[k - 1] -= 1
                else:
                    break
            else:
                break
print(*R)
