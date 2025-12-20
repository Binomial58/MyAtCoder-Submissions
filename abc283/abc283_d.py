# from collections import deque

s = input()
# Q = deque()
S = [set() for i in range(len(s))]
c = 0
for i in range(len(s)):
    if s[i] == ")":
        S[c] = set()
        c -= 1
    elif s[i] == "(":
        c += 1
        S[c] |= S[c - 1]
    else:
        if s[i] in S[c]:
            print("No")
            exit()
        else:
            S[c].add(s[i])
print("Yes")