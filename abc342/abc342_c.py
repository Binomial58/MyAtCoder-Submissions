n = int(input())
s = list(input())
q = int(input())
D = ["" for i in range(26)]
R = []
for i in range(26):
    D[i] = chr(97 + i)
for i in range(q):
    c, d = map(str, input().split())
    for j in range(26):
        if D[j] == c:
            D[j] = d
for t in s:
    R.append(D[ord(t) - 97])
print("".join(R))
# print(D)