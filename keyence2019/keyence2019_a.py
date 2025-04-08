N=list(map(int, input().split()))
if N.count(1)==1 and N.count(9)==1 and N.count(7)==1 and N.count(4)==1:
    print("YES")
else:
    print("NO")