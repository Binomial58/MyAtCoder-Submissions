n = int(input())
D = list(map(int, input().split()))
for i in range(n - 1):
    R = [D[i] for i in range(i, n - 1)]
    Rs = [R[0]]
    for j in range(len(R) - 1):
        Rs.append(Rs[-1] + R[j + 1])
    print(*Rs)
