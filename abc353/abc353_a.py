N=int(input())
H=list(map(int, input().split()))
if H[0]==max(H):
    print("-1")
else:
    for k in range(len(H)):
        if H[k]>H[0]:
            print(k+1)
            break