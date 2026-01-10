n, m, x, y = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
if max(X) < min(Y) and max(X) < y and min(Y) > x:
    print("No War")
else:
    print("War")
