n = int(input())
S = []
n -= 1
while n >= 5:
    S.append(n % 5)
    n //= 5
S.append(n)
s = 0
for i in range(len(S)):
    s += 2 * S[i] * 10**i
print(s)
