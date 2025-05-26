N=int(input())
T=""
while N!=0:
    if N%2==0:
        N//=2
        T+="B"
    else:
        N-=1
        T+="A"
print(T[::-1])