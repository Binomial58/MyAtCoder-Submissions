N=int(input())
A=list(map(int, input().split()))
B=[i for i in range(1,N+1)]
#Aをキーにして二つをソート
A,B= zip(*sorted(zip(A, B)))
print(*B)