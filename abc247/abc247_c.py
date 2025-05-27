N=int(input())
def onetwo(N):
    if N==1:
        return [1]
    else:
        return [*onetwo(N-1),N,*onetwo(N-1)]
print(*onetwo(N))