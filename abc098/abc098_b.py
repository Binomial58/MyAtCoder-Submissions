n = int(input())
s = input()
S = [t for t in s]
m = 0
for i in range(n - 1):
    T = set(S[: i + 1])
    U = set(S[i + 1 :])
    m = max(m, len(T & U))
print(m)
