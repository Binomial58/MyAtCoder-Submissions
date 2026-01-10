n = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
B = dict()
R = []
for i in range(n):
    B[Q[i]] = i + 1
for i in range(n):
    R.append(Q[P[B[i + 1] - 1] - 1])
# print(B)
print(*R)
