q, h, s, d = map(int, input().split())
n = int(input())
# 1リットル作るのにかかる最小のコスト
a = min(4 * q, 2 * q + h, h * 2, s)
# 2リットル作るのにかかる最小のコスト
b = min(a * 2, d)
print((n // 2) * b + (n % 2) * a)
