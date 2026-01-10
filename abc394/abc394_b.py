n = int(input())
S = []
for i in range(n):
    s = input()
    S.append([s, len(s)])
S = sorted(S, reverse=True, key=lambda x: -x[1])
R = []
for i in range(n):
    R.append(S[i][0])
print("".join(R))
