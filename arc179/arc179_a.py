n, k = map(int, input().split())
A = list(map(int, input().split()))
if k > 0:
    print("Yes")
    A.sort()
    print(*A)
else:
    if sum(A) >= k:
        print("Yes")
        A.sort(reverse=True)
        print(*A)
    else:
        print("No")
