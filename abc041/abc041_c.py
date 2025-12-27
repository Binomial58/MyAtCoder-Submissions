n = int(input())
A = list(map(int, input().split()))
B = []
for i in range(n):
    B.append([A[i], i + 1])
# sorted関数を用いた2次元配列のソート方法
B = sorted(B, reverse=True, key=lambda x: x[0])
for b in B:
    print(b[1])
