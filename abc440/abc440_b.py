n = int(input())
T = []
K = list(map(int, input().split()))
for i in range(n):
    T.append([K[i], i + 1])
T = sorted(T, reverse=True, key=lambda x: -x[0])
print(T[0][1], T[1][1], T[2][1])
