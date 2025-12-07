t = int(input())
R = ["No" for i in range(t)]
for i in range(t):
    n = int(input())
    s = input()
    for j in range(1, n):
        # print(s[:j], s[j:])
        if s[:j] < s[j:]:
            R[i] = "Yes"
            break
for r in R:
    print(r)
