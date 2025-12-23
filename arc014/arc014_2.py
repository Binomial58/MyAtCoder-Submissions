n = int(input())
W = []
for i in range(n):
    W.append(input())
S = set()
S.add(W[0])
for i in range(1, n):
    if W[i] in S or W[i - 1][-1] != W[i][0]:
        if i % 2 == 0:
            print("LOSE")
            exit()
        else:
            print("WIN")
            exit()
    S.add(W[i])
print("DRAW")
