h, w = map(int, input().split())
A = [list(input()) for _ in range(h)]
B = []
C = ["." for i in range(w)]
for a in A:
    if a != C:
        B.append(a)
R = [[] for i in range(len(B))]
for i in range(w):
    c = 0
    for j in range(len(B)):
        if B[j][i] == ".":
            c += 1
    if c != len(B):
        for j in range(len(B)):
            R[j].append(B[j][i])
for r in R:
    print("".join(r))
