s = input()
S = [int(s[0]), int(s[-1])]
if S[1] == 8:
    S[0] += 1
    S[1] = 1
else:
    S[1] += 1
print(str(S[0]) + "-" + str(S[1]))
