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

n=int(input())
A=list(map(int, input().split()))
B=[0 for i in range(n)]
seg=SegTree(B,lambda x,y:x+y,0)
count=0
for i in range(n):
    seg.update(A[i]-1,1)
    count+=seg.query(A[i],n)
print(count)