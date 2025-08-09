l,r=map(int, input().split())
L=list(map(int, input().split()))
R=list(map(int, input().split()))
S=set(L)
c=0
for s in S:
    c+=min(L.count(s),R.count(s))
print(c)