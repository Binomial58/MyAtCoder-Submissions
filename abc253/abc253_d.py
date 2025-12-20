import math

n, a, b = map(int, input().split())
an = n // a
bn = n // b
cn = n // (math.lcm(a, b))
S = (1 + n) * n // 2
Sa = a * (an + 1) * an // 2
Sb = b * (bn + 1) * bn // 2
Sc = math.lcm(a, b) * (cn + 1) * cn // 2
print(S - Sa - Sb + Sc)