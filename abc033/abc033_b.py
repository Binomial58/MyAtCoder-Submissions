n=int(input())
town=[[],[]]
for i in range(n):
    s,p=map(str, input().split())
    town[0].append(s)
    town[1].append(int(p))
s=sum(town[1])//2
for i in range(n):
    if town[1][i]>s:
        print(town[0][i])
        exit()
print("atcoder")

