from collections import deque

s = input()
# Q = deque()
R = deque()
# N = ["A", "B", "C"]
for i in range(len(s)):
    R.append(s[i])
    # id = N.index(s[i])
    # if i % 3 == 0:
    #     Q.append(N[(id + 2) % 3])
    # elif i % 3 == 1:
    #     Q.append(N[(id + 1) % 3])
    # else:
    #     Q.append(s[i])
    if (
        len(R) >= 3
        and R[len(R) - 1] == "C"
        and R[len(R) - 2] == "B"
        and R[len(R) - 3] == "A"
    ):
        for k in range(3):
            R.pop()
# print(Q)
print("".join(R))
