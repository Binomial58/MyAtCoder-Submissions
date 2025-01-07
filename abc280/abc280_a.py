H,W=map(int, input().split())
S=0
for _ in range(H):
    T=input()
    S+=T.count("#")
print(S)