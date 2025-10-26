n,m=map(int, input().split())
for i in range(min(n,m)):
    print("OK")
for j in range(n-m):
    print("Too Many Requests")