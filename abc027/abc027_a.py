L=list(map(int, input().split()))
for l in set(L):
    if L.count(l)==1 or L.count(l)==3:
        print(l)