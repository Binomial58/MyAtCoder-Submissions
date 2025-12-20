import math


# lからrまでの中にnの倍数は何個入るのか
def div(r, l, n):
    if r % n == 0:
        return l // n - r // n + 1
    else:
        return l // n - r // n


a, b, c, d = map(int, input().split())
n = b - a + 1
# print(n)
# print(div(a, b, c))
# print(div(a, b, d))
# print(div(a, b, math.lcm(c, d)))
print(n - div(a, b, c) - div(a, b, d) + div(a, b, math.lcm(c, d)))