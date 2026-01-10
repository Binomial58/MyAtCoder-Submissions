n, m = map(int, input().split())
R = [0 for i in range(n)]
S = []
for i in range(n):
    S.append(input())
for i in range(m):
    zero = 0
    one = 0
    for j in range(n):
        if S[j][i] == "1":
            one += 1
        else:
            zero += 1
    # print(zero, one)
    if one == n or zero == n:
        for j in range(n):
            R[j] += 1
    elif one > zero:
        for j in range(n):
            if S[j][i] == "0":
                R[j] += 1
    else:
        for j in range(n):
            if S[j][i] == "1":
                R[j] += 1
T = []
for j in range(n):
    if R[j] == max(R):
        T.append(j + 1)
print(*T)
