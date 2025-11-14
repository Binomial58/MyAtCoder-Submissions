n = int(input())
W = list(map(str, input().split()))
Check = ["TAKAHASHIKUN", "Takahashikun", "takahashikun"]
count = 0
for i in range(n):
    if i != n - 1:
        w = W[i]
    else:
        w = W[i][: len(W[i]) - 1]
    if w in Check:
        count += 1
print(count)
