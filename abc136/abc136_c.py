n = int(input())
H = list(map(int, input().split()))
H[0] -= 1
for i in range(n - 1):
    if H[i + 1] > H[i]:
        H[i + 1] -= 1
    if H[i + 1] < H[i]:
        print("No")
        exit()
print("Yes")
