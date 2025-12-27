import math


def dis(xa, ya, xb, yb):
    return math.sqrt((xa - xb) ** 2 + (ya - yb) ** 2)


D = list(map(int, input().split()))
T = [
    dis(D[0], D[1], D[2], D[3]),
    dis(D[2], D[3], D[4], D[5]),
    dis(D[4], D[5], D[0], D[1]),
]
s = (T[0] + T[1] + T[2]) / 2
print(math.sqrt(s * (s - T[0]) * (s - T[1]) * (s - T[2])))
