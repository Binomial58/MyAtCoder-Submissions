from collections import Counter

n = int(input())
D = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))
C = Counter(D)
for t in T:
    if t in C:
        C[t] -= 1
        if C[t] == 0:
            del C[t]
    else:
        print("NO")
        exit()
print("YES")
