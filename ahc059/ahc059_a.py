import sys
import time
import random
import math

input = sys.stdin.readline

# =====================
# 入力
# =====================
N = int(input())
A0 = [list(map(int, input().split())) for _ in range(N)]
M = N * N

# 盤面に存在する番号の集合（ケース依存）
vals = []
mx = -1
for i in range(N):
    for j in range(N):
        if A0[i][j] > mx:
            mx = A0[i][j]
V = mx + 1

pos = [[] for _ in range(V)]
for i in range(N):
    for j in range(N):
        pos[A0[i][j]].append((i, j))

# 「ちょうど2回」のはずだが，安全のため存在するものだけ集める
for v in range(V):
    if len(pos[v]) == 2:
        vals.append(v)

# =====================
# 初期解：ジグザグ巡回
# =====================
path = []
for i in range(N):
    if i % 2 == 0:
        for j in range(N):
            path.append((i, j))
    else:
        for j in range(N - 1, -1, -1):
            path.append((i, j))

# 位置→index（高速化）
idx = [[0] * N for _ in range(N)]
for k, (i, j) in enumerate(path):
    idx[i][j] = k

# act: 0=Z，1=NOP
act = [0] * M

# =====================
# 評価（シミュレーション）
#   E = 10*Smax + 1000*remain
# =====================
def evaluate(path, act):
    # board をコピー（-1 を空として使う）
    board = [row[:] for row in A0]
    stack = []
    smax = 0

    for k in range(M):
        i, j = path[k]
        if act[k] == 0 and board[i][j] != -1:
            v = board[i][j]
            board[i][j] = -1
            stack.append(v)
            if len(stack) >= 2 and stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
        if len(stack) > smax:
            smax = len(stack)

    remain = len(stack)
    for i in range(N):
        for j in range(N):
            if board[i][j] != -1:
                remain += 1

    return 10 * smax + 1000 * remain, smax, remain

cur_score, _, _ = evaluate(path, act)
best_score = cur_score
best_path = path[:]
best_act = act[:]

# =====================
# 焼きなまし
# =====================
TIME_LIMIT = 1.8
start = time.time()

T0 = 200.0
T1 = 1.0

while True:
    now = time.time()
    if now - start > TIME_LIMIT:
        break

    t = (now - start) / TIME_LIMIT
    T = T0 * (1 - t) + T1 * t

    r = random.random()

    new_path = path[:]
    new_act = act[:]  # act も状態に含める
    new_idx = [row[:] for row in idx]

    # --- 近傍1：ペア寄せ swap（存在する番号から選ぶ） ---
    if r < 0.7:
        v = random.choice(vals)
        (x1, y1), (x2, y2) = pos[v]
        p1 = new_idx[x1][y1]
        p2 = new_idx[x2][y2]
        if p1 > p2:
            p1, p2 = p2, p1
        if p2 - p1 > 1:
            q = p1 + 1

            (a1, b1) = new_path[q]
            (a2, b2) = new_path[p2]

            new_path[q], new_path[p2] = new_path[p2], new_path[q]
            new_idx[a1][b1], new_idx[a2][b2] = p2, q

            new_act[q], new_act[p2] = new_act[p2], new_act[q]

    # --- 近傍2：区間 reverse ---
    elif r < 0.9:
        i = random.randint(0, M - 2)
        j = random.randint(i + 1, M - 1)
        new_path[i:j] = reversed(new_path[i:j])
        new_act[i:j] = reversed(new_act[i:j])

        # idx を更新（区間だけ直す）
        for k in range(i, j):
            x, y = new_path[k]
            new_idx[x][y] = k

    # --- 近傍3：Z / NOP 切替 ---
    else:
        k = random.randrange(M)
        new_act[k] ^= 1

    new_score, _, _ = evaluate(new_path, new_act)
    diff = new_score - cur_score

    if diff < 0 or random.random() < math.exp(-diff / T):
        path = new_path
        act = new_act
        idx = new_idx
        cur_score = new_score

        if cur_score < best_score:
            best_score = cur_score
            best_path = path[:]
            best_act = act[:]

# =====================
# 操作列生成（移動＋Z のみ）: 必ず合法移動で繋ぐ
# =====================

def move_ops(x, y, nx, ny):
    res = []
    while x < nx:
        res.append("D")
        x += 1
    while x > nx:
        res.append("U")
        x -= 1
    while y < ny:
        res.append("R")
        y += 1
    while y > ny:
        res.append("L")
        y -= 1
    return res

ops = []
x, y = 0, 0

# best_path[0] が (0,0) でない可能性があるので，最初も移動で合わせる
sx, sy = best_path[0]
ops.extend(move_ops(x, y, sx, sy))
x, y = sx, sy

if best_act[0] == 0 and A0[x][y] != -1:
    ops.append("Z")

for k in range(1, M):
    nx, ny = best_path[k]
    ops.extend(move_ops(x, y, nx, ny))
    x, y = nx, ny

    # NOP のときは何もしない
    if best_act[k] == 0:
        ops.append("Z")

# 操作回数上限対策：超えていたら安全に自明解へフォールバック
if len(ops) > 2 * (N ** 3):
    ops = []
    # ジグザグで必ず完答する自明解
    ops.append("Z")
    for i in range(N):
        if i % 2 == 0:
            for _ in range(N - 1):
                ops.append("R")
                ops.append("Z")
        else:
            for _ in range(N - 1):
                ops.append("L")
                ops.append("Z")
        if i != N - 1:
            ops.append("D")
            ops.append("Z")

print("\n".join(ops))