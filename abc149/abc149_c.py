#高速素数判定法
def inPrime(n):
    for i in range(2,n+1):
        #ルートnまでの数を見ればよい
        if i*i>n:
            return True
        #割り切れた場合は素数ではない
        if n%i==0:
            return False
X=int(input())
while True:
    if inPrime(X):
        print(X)
        exit()
    X+=1