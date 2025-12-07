n = int(input())
R = [0 for i in range(6)]
for i in range(n):
    M, m = map(float, input().split())
    if M >= 35:
        R[0] += 1
    if 30 <= M < 35:
        R[1] += 1
    if 25 <= M < 30:
        R[2] += 1
    if m >= 25:
        R[3] += 1
    if m < 0 and M >= 0:
        R[4] += 1
    if M < 0:
        R[5] += 1
print(*R)
