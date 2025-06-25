H,W=map(int, input().split())
B=[]
B.append("#"*(W+2))
for i in range(H):
    s=input()
    B.append("#"+s+"#")
B.append("#"*(W+2))
for b in B:
    print(b)