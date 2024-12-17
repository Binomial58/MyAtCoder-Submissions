N=int(input())
A=set(list(map(int, input().split())))
A.remove(max(A))
print(max(A))