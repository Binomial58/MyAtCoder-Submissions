n = int(input())
R = list(map(int, input().split()))
C = list(map(int, input().split()))
q = int(input())
S = []
for i in range(q):
    r, c = map(int, input().split())
    a = R[r - 1]
    b = C[c - 1]
    if a + b > n:
        S.append("#")
    else:
        S.append(".")
print("".join(S))
