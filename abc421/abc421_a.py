n = int(input())
S = []
for i in range(n):
    S.append(input())
x, y = map(str, input().split())
if S[int(x) - 1] == y:
    print("Yes")
else:
    print("No")
