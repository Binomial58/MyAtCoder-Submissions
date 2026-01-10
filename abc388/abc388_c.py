import bisect

n = int(input())
A = list(map(int, input().split()))
count = 0
for a in A:
    count += n - bisect.bisect_left(A, a * 2)
print(count)
