s = input()
n = int(input())
Now = [i for i in range(len(s))]
R = []
for i in range(n):
    l, r = map(int, input().split())
    D = Now[l - 1 : r]
    k = 0
    for j in range(r - 1, l - 2, -1):
        Now[j] = D[k]
        k += 1
    # print(D)
for i in Now:
    R.append(s[i])
print("".join(R))
