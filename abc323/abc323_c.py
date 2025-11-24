n, m = map(int, input().split())
A = list(map(int, input().split()))
S = []
SC = [i + 1 for i in range(n)]
NT = [[] for i in range(n)]
for i in range(n):
    s = input()
    S.append(s)
    for j in range(m):
        if s[j] == "x":
            NT[i].append(A[j])
        else:
            SC[i] += A[j]
# print(NT)
for i in range(n):
    if SC[i] >= max(SC):
        print(0)
        continue
    k = 1
    NT[i].sort(reverse=True)
    # print(NT[1][:k])
    for j in range(len(NT)):
        if SC[i] + sum(NT[i][:k]) >= max(SC):
            print(k)
            break
        k += 1
# print(NT)
# print(SC)
