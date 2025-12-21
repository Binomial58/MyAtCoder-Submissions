class UnionFind:
    def __init__(self, n):
        self.n = n
        self.P = [-1] * n

    def find(self, x):
        if self.P[x] < 0:
            return x
        else:
            self.P[x] = self.find(self.P[x])
            return self.P[x]

    # xとyを結ぶ
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.P[x] > self.P[y]:
            x, y = y, x
        self.P[x] += self.P[y]
        self.P[y] = x

    def size(self, x):
        return -self.P[self.find(x)]

    # xとyが同じ親か調べる
    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.P) if x < 0]

    def group_cnt(self):
        return len(self.roots())

    def group_and_members(self):
        group_info = dict()
        for member in range(self.n):
            g_id = self.find(member)
            if g_id not in group_info:
                group_info[g_id] = []
            group_info[g_id].append(member)
        return group_info


n, q = map(int, input().split())
uf = UnionFind(n)
R = []
for i in range(q):
    query = list(map(int, input().split()))
    u = query[1]
    v = query[2]
    if query[0] == 1:
        uf.union(u - 1, v - 1)
    else:
        if uf.same(u - 1, v - 1):
            R.append("Yes")
        else:
            R.append("No")
for r in R:
    print(r)
