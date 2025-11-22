n = int(input())
a, b = map(int, input().split())
k = int(input())
P = list(map(int, input().split()))
if len(set(P)) == k and a not in P and b not in P:
    print("YES")
else:
    print("NO")
