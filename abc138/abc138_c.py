N=int(input())
V=list(map(int, input().split()))
V.sort(reverse=True)
for i in range(N-1):
    x=(V[len(V)-1]+V[len(V)-2])/2
    V.pop()
    V.pop()
    V.append(x)
print(V[0])