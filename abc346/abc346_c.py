N,K=map(int, input().split())
A=set(list(map(int, input().split())))
#Aの中のK以下の値のみを抽出
B={x for x in A if x<=K}
S=K*(K+1)//2
print(S-sum(B))