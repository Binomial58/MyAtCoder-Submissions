class UnionFind:
    def __init__(self, n):
        self.n = n
        self.P = [-1] * n  # parents

    def find(self, x):
        if self.P[x] < 0:
            return x
        self.P[x] = self.find(self.P[x])
        return self.P[x]

    # xとyを繋げる
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

    # xとyが同じ親かを判定する
    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.P) if x < 0]

    # グループの数を出力
    def group_cnt(self):
        return len(self.roots())

    # どの頂点がどのグループにいるのかの一覧
    def group_and_members(self):
        group_info = dict()
        for member in range(self.n):
            g_id = self.find(member)
            if g_id not in group_info:
                group_info[g_id] = []
            group_info[g_id].append(member)
        return group_info


# uf=UnionFind(n) のように宣言する

n = int(input())
E = dict()
uf = UnionFind(n)
vec = [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, 0), (1, 1)]
for i in range(n):
    x, y = map(int, input().split())
    E[(x, y)] = i
for e in E:
    x, y = e
    for vx, vy in vec:
        dx = x + vx
        dy = y + vy
        if (dx, dy) in E:
            uf.union(E[(x, y)], E[dx, dy])
# print(E)
print(uf.group_cnt())
