#include <bits/stdc++.h>
using namespace std;

static const int INF = 1e9;

static vector<vector<int>> compute_dist(int N, const vector<vector<int>> &adj) {
    vector<vector<int>> dist(N, vector<int>(N, INF));
    for (int s = 0; s < N; ++s) {
        queue<int> q;
        dist[s][s] = 0;
        q.push(s);
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (int v : adj[u]) {
                if (dist[s][v] == INF) {
                    dist[s][v] = dist[s][u] + 1;
                    q.push(v);
                }
            }
        }
    }
    return dist;
}

static vector<int> build_shop_order(int K, const vector<vector<int>> &dist) {
    vector<int> order;
    order.reserve(K);
    vector<char> used(K, 0);
    int cur = 0;
    order.push_back(cur);
    used[cur] = 1;
    for (int it = 1; it < K; ++it) {
        int best = -1;
        int bestd = INF;
        for (int s = 0; s < K; ++s) {
            if (used[s]) continue;
            if (dist[cur][s] < bestd) {
                bestd = dist[cur][s];
                best = s;
            }
        }
        if (best == -1) break;
        used[best] = 1;
        order.push_back(best);
        cur = best;
    }
    return order;
}

static uint64_t hash_path(const vector<int> &path) {
    uint64_t h = 1469598103934665603ULL;
    for (int x : path) {
        h ^= (uint64_t)(x + 1);
        h *= 1099511628211ULL;
    }
    return h;
}

static vector<vector<int>> build_loops_for_shop(
    int shop,
    int K,
    const vector<vector<int>> &adj
) {
    vector<int> neigh_trees;
    for (int v : adj[shop]) {
        if (v >= K) neigh_trees.push_back(v);
    }
    vector<vector<int>> loops;
    if ((int)neigh_trees.size() < 2) return loops;

    unordered_set<uint64_t> seen;
    const int N = (int)adj.size();
    vector<int> dist(N, -1), parent(N, -1);

    for (int u : neigh_trees) {
        fill(dist.begin(), dist.end(), -1);
        fill(parent.begin(), parent.end(), -1);
        queue<int> q;
        dist[u] = 0;
        q.push(u);
        while (!q.empty()) {
            int x = q.front();
            q.pop();
            for (int y : adj[x]) {
                if (y < K) continue;
                if (dist[y] == -1) {
                    dist[y] = dist[x] + 1;
                    parent[y] = x;
                    q.push(y);
                }
            }
        }

        for (int v : neigh_trees) {
            if (v == u) continue;
            if (dist[v] == -1) continue;
            vector<int> path;
            int t = v;
            while (t != -1) {
                path.push_back(t);
                if (t == u) break;
                t = parent[t];
            }
            if (path.back() != u) continue;
            reverse(path.begin(), path.end());
            path.push_back(shop);

            uint64_t h1 = hash_path(path);
            vector<int> rev = path;
            rev.pop_back();
            reverse(rev.begin(), rev.end());
            rev.push_back(shop);
            uint64_t h2 = hash_path(rev);
            uint64_t key = min(h1, h2);
            if (seen.insert(key).second) {
                loops.push_back(path);
            }
        }
    }

    sort(loops.begin(), loops.end(),
         [](const vector<int> &a, const vector<int> &b) {
             return a.size() < b.size();
         });
    if ((int)loops.size() > 2) loops.resize(2);
    return loops;
}

static vector<int> pick_loop_path(
    int shop,
    int prev,
    const vector<vector<int>> &loops,
    int visit_cnt
) {
    if (loops.empty()) return {};
    int n = (int)loops.size();
    int start = visit_cnt % n;
    for (int i = 0; i < n; ++i) {
        const auto &p = loops[(start + i) % n];
        if (!p.empty() && p[0] != prev) return p;
        vector<int> rev = p;
        rev.pop_back();
        reverse(rev.begin(), rev.end());
        rev.push_back(shop);
        if (!rev.empty() && rev[0] != prev) return rev;
    }
    return {};
}

static vector<int> path_no_backtrack(
    int cur,
    int prev,
    int target,
    const vector<vector<int>> &adj,
    const vector<char> &is_shop,
    bool avoid_other_shops
) {
    if (cur == target) return {};
    const int N = (int)adj.size();
    const int P = N + 1;
    const int prev_idx = (prev == -1 ? N : prev);
    const int start = prev_idx * N + cur;
    vector<int> dist(P * N, -1), par(P * N, -1);
    queue<int> q;
    dist[start] = 0;
    q.push(start);
    int found = -1;

    while (!q.empty()) {
        int s = q.front();
        q.pop();
        int pidx = s / N;
        int u = s % N;
        int prev_node = (pidx == N ? -1 : pidx);
        if (u == target) {
            found = s;
            break;
        }
        for (int v : adj[u]) {
            if (v == prev_node) continue;
            if (avoid_other_shops && is_shop[v] && v != target) continue;
            int ns = u * N + v;
            if (dist[ns] == -1) {
                dist[ns] = dist[s] + 1;
                par[ns] = s;
                q.push(ns);
            }
        }
    }

    if (found == -1) return {};
    vector<int> path;
    for (int s = found; s != start; s = par[s]) {
        path.push_back(s % N);
    }
    reverse(path.begin(), path.end());
    return path;
}

static vector<int> select_path(
    int cur,
    int prev,
    int target,
    const vector<vector<int>> &adj,
    const vector<char> &is_shop,
    int avoid_mode,
    int auto_margin
) {
    if (avoid_mode == 2) {
        return path_no_backtrack(cur, prev, target, adj, is_shop, false);
    }
    if (avoid_mode == 1) {
        auto p = path_no_backtrack(cur, prev, target, adj, is_shop, true);
        if (!p.empty()) return p;
        return path_no_backtrack(cur, prev, target, adj, is_shop, false);
    }
    auto p_avoid = path_no_backtrack(cur, prev, target, adj, is_shop, true);
    auto p_allow = path_no_backtrack(cur, prev, target, adj, is_shop, false);
    if (p_avoid.empty()) return p_allow;
    if (p_allow.empty()) return p_avoid;
    if ((int)p_avoid.size() <= (int)p_allow.size() + auto_margin) return p_avoid;
    return p_allow;
}

int main(int argc, char **argv) {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // パラメータ（ローカル実験用）
    double r_ratio = 0.40;
    int loop_base = 0;
    int loop_extra = 1;
    int loop_max = 2;
    int avoid_mode = 2;   // 0:自動 1:回避ON 2:回避OFF
    int auto_margin = 2;  // 自動時に回避経路を選ぶ許容差
    for (int i = 1; i < argc; ++i) {
        string s = argv[i];
        if (s.rfind("--r=", 0) == 0) {
            r_ratio = stod(s.substr(4));
        } else if (s.rfind("--loop=", 0) == 0) {
            loop_base = stoi(s.substr(7));
        } else if (s.rfind("--loop-extra=", 0) == 0) {
            loop_extra = stoi(s.substr(13));
        } else if (s.rfind("--loop-max=", 0) == 0) {
            loop_max = stoi(s.substr(11));
        } else if (s.rfind("--avoid=", 0) == 0) {
            string v = s.substr(8);
            if (v == "on") avoid_mode = 1;
            else if (v == "off") avoid_mode = 2;
            else avoid_mode = 0;
        } else if (s.rfind("--avoid-margin=", 0) == 0) {
            auto_margin = stoi(s.substr(15));
        }
    }
    r_ratio = min(1.0, max(0.0, r_ratio));
    loop_base = max(0, loop_base);
    loop_extra = max(0, loop_extra);
    loop_max = max(loop_max, loop_base + loop_extra);
    auto_margin = max(0, auto_margin);
    if (avoid_mode < 0 || avoid_mode > 2) avoid_mode = 0;

    int N, M, K, T;
    if (!(cin >> N >> M >> K >> T)) return 0;

    vector<vector<int>> adj(N);
    for (int i = 0; i < M; ++i) {
        int a, b;
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    for (int i = 0; i < N; ++i) {
        int x, y;
        cin >> x >> y;
    }

    vector<char> is_shop(N, 0);
    for (int i = 0; i < K; ++i) is_shop[i] = 1;

    // 前処理（全点距離とショップ巡回順）
    auto dist = compute_dist(N, adj);
    vector<int> shop_order = build_shop_order(K, dist);
    vector<int> shop_pos(K, 0);
    for (int i = 0; i < (int)shop_order.size(); ++i) shop_pos[shop_order[i]] = i;

    // 各ショップ周辺の小ループ（木のみのサイクル）を構築
    vector<vector<vector<int>>> loops(K);
    for (int s = 0; s < K; ++s) {
        loops[s] = build_loops_for_shop(s, K, adj);
    }

    // R 化する木を決定（ショップに近い木を優先）
    vector<char> flavor(N, 'W');
    vector<char> flipped(N, 0);
    vector<char> plan_flip(N, 0);
    vector<pair<int, int>> rank;
    rank.reserve(N - K);
    for (int v = K; v < N; ++v) {
        int bestd = INF;
        for (int s = 0; s < K; ++s) bestd = min(bestd, dist[v][s]);
        rank.emplace_back(bestd, v);
    }
    sort(rank.begin(), rank.end());
    int target_r = (int)round((N - K) * r_ratio);
    for (int i = 0; i < target_r && i < (int)rank.size(); ++i) {
        plan_flip[rank[i].second] = 1;
    }

    // 納品済み管理（ハッシュのみ）
    vector<unordered_set<uint64_t>> delivered(K);
    vector<int> visit_cnt(K, 0);
    uint64_t base = 1000003ULL;
    uint64_t h = 0;
    int len = 0;

    auto append_flavor = [&](int v) {
        uint64_t x = (flavor[v] == 'W') ? 1ULL : 2ULL;
        h = h * base + x;
        ++len;
    };
    auto hash_key = [&](uint64_t hh, int ll) {
        uint64_t x = hh ^ (uint64_t)(ll) * 0x9e3779b97f4a7c15ULL;
        x ^= (uint64_t)(ll) << 32;
        return x;
    };

    int cur = 0;
    int prev = -1;
    int steps = 0;

    deque<int> plan;
    bool plan_is_loop = false;
    int loop_remaining = 0;

    while (steps < T) {
        // 行動2: 予定された木なら R 化
        if (cur >= K && flavor[cur] == 'W' && plan_flip[cur] && !flipped[cur]) {
            cout << -1 << '\n';
            flavor[cur] = 'R';
            flipped[cur] = 1;
            ++steps;
            continue;
        }

        if (plan.empty()) {
            if (cur < K) {
                if (loop_remaining > 0 && !loops[cur].empty()) {
                    auto loop_path = pick_loop_path(cur, prev, loops[cur], visit_cnt[cur]);
                    if (!loop_path.empty()) {
                        plan = deque<int>(loop_path.begin(), loop_path.end());
                        plan_is_loop = true;
                    } else {
                        loop_remaining = 0;
                    }
                }
                if (plan.empty()) {
                    int pos = shop_pos[cur];
                    int target = shop_order[(pos + 1) % K];
                    auto path = select_path(cur, prev, target, adj, is_shop, avoid_mode, auto_margin);
                    plan = deque<int>(path.begin(), path.end());
                    plan_is_loop = false;
                }
            } else {
                int target = 0;
                int bestd = INF;
                for (int s = 0; s < K; ++s) {
                    if (dist[cur][s] < bestd) {
                        bestd = dist[cur][s];
                        target = s;
                    }
                }
                auto path = select_path(cur, prev, target, adj, is_shop, avoid_mode, auto_margin);
                plan = deque<int>(path.begin(), path.end());
                plan_is_loop = false;
            }

            if (plan.empty()) break;
        }

        int nxt = plan.front();
        plan.pop_front();
        cout << nxt << '\n';
        ++steps;
        prev = cur;
        cur = nxt;

        if (cur >= K) {
            append_flavor(cur);
        } else {
            uint64_t key = hash_key(h, len);
            bool inserted = delivered[cur].insert(key).second;
            visit_cnt[cur]++;
            h = 0;
            len = 0;

            if (plan.empty()) {
                if (plan_is_loop) {
                    if (loop_remaining > 0) loop_remaining--;
                } else {
                    loop_remaining = loop_base;
                }
                if (!inserted) loop_remaining += loop_extra;
                if (loop_remaining > loop_max) loop_remaining = loop_max;
            }
        }
    }

    return 0;
}
