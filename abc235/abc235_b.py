N=int(input())
H=list(map(int, input().split()))
a=H[0]
for i in range(N-1):
    if H[i+1]>a:
        a=H[i+1]
    else:
        print(a)
        exit()
print(a)