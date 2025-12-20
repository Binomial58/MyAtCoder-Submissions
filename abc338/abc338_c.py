n = int(input())
Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
m = 0
for i in range(max(Q) + 1):
    now = 10**10
    for j in range(n):
        if Q[j] - A[j] * i < 0:
            print(m)
            exit()
        if B[j] != 0:
            now = min(now, (Q[j] - A[j] * i) // B[j])
    m = max(m, i + now)
print(m)
