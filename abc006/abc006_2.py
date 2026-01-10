n = int(input())
R = [0, 0, 1]
if n <= 3:
    print(R[n - 1])
else:
    for i in range(n - 3):
        k = len(R)
        R.append((R[k - 1] + R[k - 2] + R[k - 3]) % (10007))
    # print(R)
    print(R[-1])
