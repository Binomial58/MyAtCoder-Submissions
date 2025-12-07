A = ["a", "t", "c", "o", "d", "e", "r"]
s = input()
S = []
for a in s:
    S.append(A.index(a))
# print(S)
count = 0
for i in range(len(s)):
    for j in range(i, len(s)):
        if S[i] > S[j]:
            count += 1
print(count)
