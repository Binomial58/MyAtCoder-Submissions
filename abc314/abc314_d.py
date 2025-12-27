n = int(input())
S = list(input())
q = int(input())
Q = []
for i in range(q):
    Q.append(list(map(str, input().split())))
last = -1
for i in range(q - 1, -1, -1):
    if Q[i][0] != "1":
        break
last = i
for i in range(q):
    if Q[i][0] == "1":
        S[int(Q[i][1]) - 1] = Q[i][2]
    else:
        if i == last:
            if Q[i][0] == "2":
                for j in range(n):
                    S[j] = S[j].lower()
            else:
                for j in range(n):
                    S[j] = S[j].upper()
    # print(S)
print("".join(S))
