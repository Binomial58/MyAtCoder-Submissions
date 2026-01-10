n, s = map(int, input().split())
T = list(map(int, input().split()))
now = s
for i in range(n):
    if now >= T[i]:
        now = T[i] + s
    else:
        print("No")
        exit()
print("Yes")
