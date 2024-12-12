N=int(input())
A=[]
for k in range(1,N+1):
    if k%3==0:
        A.append("x")
    else:
        A.append("o")
#リストを空白なしで表示
print("".join([str(n) for n in A]))