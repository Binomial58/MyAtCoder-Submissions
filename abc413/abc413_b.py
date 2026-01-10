n = int(input())
S = []
R = set()
for i in range(n):
    S.append(input())
for i in range(n):
    for j in range(n):
        if i != j:
            R.add(S[i] + S[j])
print(len(R))
