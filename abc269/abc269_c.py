n = int(input())
T = []
while n >= 2:
    T.append(n % 2)
    n //= 2
T.append(n)
T = T[::-1]
R = []
for i in range(len(T)):
    if T[i] == 1:
        R.append(i)
# print(R)
for i in range(2 ** len(R)):
    S = []
    while i >= 2:
        S.append(i % 2)
        i //= 2
    S.append(i)
    for k in range(len(R) - len(S)):
        S.append(0)
    S = S[::-1]
    ans = ""
    # print(S)
    e = 0
    for j in range(len(T)):
        if j in R:
            ans += str(S[e])
            e += 1
        else:
            ans += "0"
    # print(T)
    # print(S)
    # print(ans)
    ans = ans[::-1]
    answer = 0
    for u in range(len(ans)):
        answer += 2**u * int(ans[u])
    print(answer)
