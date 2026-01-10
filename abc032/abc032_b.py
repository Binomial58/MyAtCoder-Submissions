s = input()
k = int(input())
if len(s) < k:
    print(0)
else:
    R = set()
    for i in range(len(s) - k + 1):
        R.add(s[i : i + k])
    print(len(R))
