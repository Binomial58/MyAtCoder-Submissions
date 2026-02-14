n = int(input())
S = []
maxlen = 0
for i in range(n):
    S.append(input())
    maxlen = max(len(S[-1]), maxlen)
for s in S:
    print("." * ((maxlen - len(s)) // 2) + s + "." * ((maxlen - len(s)) // 2))
# print(S)
