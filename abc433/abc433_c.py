s = input()
W = []
l = 1
a = s[0]
for i in range(1, len(s)):
    if s[i] == a:
        l += 1
    else:
        W.append([int(a), l])
        a = s[i]
        l = 1
W.append([int(a), l])
# 数字の種類，個数
# print(W)
count = 0
for i in range(len(W) - 1):
    if W[i][0] + 1 == W[i + 1][0]:
        # print(W[i], W[i + 1])
        count += min(W[i][1], W[i + 1][1])
print(count)
