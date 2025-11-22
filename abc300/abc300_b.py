h, w = map(int, input().split())
A = [list(input()) for _ in range(h)]
B = [list(input()) for _ in range(h)]
EB = [B[i] + B[i] for i in range(h)]
for i in range(h):
    EB.append(EB[i])
for a in range(h + 1):
    for b in range(w + 1):
        count = 0
        for i in range(h):
            for j in range(w):
                if A[i][j] == EB[a + i][b + j]:
                    count += 1
        if count == h * w:
            print("Yes")
            exit()
print("No")
