n = int(input())
A = list(map(int, input().split()))
count = 0
# 左から探索
L3 = dict()
L7 = dict()
for a in A:
    if a % 3 == 0:
        if a in L3:
            L3[a] += 1
        else:
            L3[a] = 1
    if a % 7 == 0:
        if a in L7:
            L7[a] += 1
        else:
            L7[a] = 1
    if a % 5 == 0:
        d = a // 5
        if d * 3 in L3 and d * 7 in L7:
            count += L3[d * 3] * L7[d * 7]
# 右から探索
R3 = dict()
R7 = dict()
B = A[::-1]
for a in B:
    if a % 3 == 0:
        if a in R3:
            R3[a] += 1
        else:
            R3[a] = 1
    if a % 7 == 0:
        if a in R7:
            R7[a] += 1
        else:
            R7[a] = 1
    if a % 5 == 0:
        d = a // 5
        if d * 3 in R3 and d * 7 in R7:
            count += R3[d * 3] * R7[d * 7]
# print(L3)
# print(L7)
print(count)
