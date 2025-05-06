def BaseK(k,n):
    S=0
    for i in range(len(str(n))):
        S+=int(str(n)[len(str(n))-i-1])*k**i
    return S
K=int(input())
A,B=map(int, input().split())
print(BaseK(K,A)*BaseK(K,B))