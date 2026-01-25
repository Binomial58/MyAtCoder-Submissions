'''
    Segment-Tree
    【説明】
        0-indexed
    【コンストラクタ】
        A    : 配列
        func : 作用させる関数
        e    : 単位元
    【メソッド】
        add(i)       : A[i] += x
        update(i, x) : A[i] = x
        query(l, r)  : func(A[l], A[l + 1], ... A[r - 1])を取得
        all_prod()   : func(A[0], A[1], ..., A[N - 1])を取得
        print()      : Aを表示
'''

class SegTree:
    def __init__(self, A, func, e):
        self.N = len(A)
        self.func = func
        self.A = A
        self.e = e
        self.num = 1 << (self.N - 1).bit_length()
        self.tree = [e] * 2 * self.num
        for i in range(self.N):
            self.tree[self.num + i] = A[i]
            
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.func(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        self.A[k] = x
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.func(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def add(self, k, x):
        self.update(k, self.A[k] + x)

    def query(self, l, r):
        ret = self.e
        l += self.num
        r += self.num

        while l < r:
            if l & 1:
                ret = self.func(ret, self.tree[l])
                l += 1
            if r & 1:
                ret = self.func(ret, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return ret

    def all_prod(self): 
        return self.tree[1]

    def print(self):
        print("[index]", " ".join(map(str, [i for i in range(self.N)])))
        print("[value]", " ".join(map(str, [self.A[i] for i in range(self.N)])))

n,q=map(int, input().split())
A=list(map(int, input().split()))
seg=SegTree(A,lambda x,y:x+y,0)
R=[]
for i in range(q):
    query=list(map(int, input().split()))
    if query[0]==1:
        x=query[1]
        p1=seg.query(x-1,x)
        p2=seg.query(x,x+1)
        # print("p1,p2",p1,p2)
        seg.update(x-1,p2)
        seg.update(x,p1)
    else:
        l,r=query[1],query[2]
        R.append(seg.query(l-1,r))
    # print("hoege",seg.all_prod())
for r in R:
    print(r)