#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using u32 = uint32_t;
using u64 = uint64_t;

#define rep0(i, n) for (int i = 0; i < (int)(n); ++i)
#define rep(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rrep(i, a, b) for (int i = (int)(a); i > (int)(b); --i)
#define srep(i, a, b, step) \
    for (long long i = (a); (step) > 0 ? i < (b) : i > (b); i += (step))

#define all(v) (v).begin(), (v).end()
#define MIN(v) *min_element(all(v))
#define MAX(v) *max_element(all(v))

const int INF = (1 << 30);
const ll INFLL = (1LL << 62);
const ll MOD = 998244353;
const ll MOD2 = 1000000007;

namespace fastio
{
    // 入力
    template <class T>
    void read(T &x) { cin >> x; }

    template <class A, class B>
    void read(pair<A, B> &p)
    {
        read(p.first);
        read(p.second);
    }

    template <size_t I = 0, class... Ts>
    inline enable_if_t<I == sizeof...(Ts)> read_tuple(tuple<Ts...> &) {}
    template <size_t I = 0, class... Ts>
        inline enable_if_t < I<sizeof...(Ts)> read_tuple(tuple<Ts...> &t)
    {
        read(get<I>(t));
        read_tuple<I + 1>(t);
    }
    template <class... Ts>
    void read(tuple<Ts...> &t) { read_tuple(t); }

    template <class T, size_t N>
    void read(array<T, N> &a)
    {
        for (auto &x : a)
            read(x);
    }
    template <class T>
    void read(vector<T> &v)
    {
        for (auto &x : v)
            read(x);
    }
    template <class T>
    void read(deque<T> &v)
    {
        for (auto &x : v)
            read(x);
    }

    template <class Head, class... Tail>
    void read(Head &head, Tail &...tail)
    {
        read(head);
        if constexpr (sizeof...(Tail))
            read(tail...);
    }

    // 基本型
    template <class T>
    void wt(const T &x) { cout << x; }

    // 小数は小数点以下10桁で固定出力
    inline void wt(float x) { cout << fixed << setprecision(10) << x; }
    inline void wt(double x) { cout << fixed << setprecision(10) << x; }
    inline void wt(long double x) { cout << fixed << setprecision(10) << x; }

    // 文字列系
    inline void wt(const char *s) { cout << s; }
    inline void wt(const string &s) { cout << s; }

    // pair
    template <class A, class B>
    void wt(const pair<A, B> &p)
    {
        wt(p.first);
        cout << ' ';
        wt(p.second);
    }

    // tuple
    template <size_t I = 0, class... Ts>
    inline enable_if_t<I == sizeof...(Ts)> wt_tuple(const tuple<Ts...> &) {}
    template <size_t I = 0, class... Ts>
        inline enable_if_t < I<sizeof...(Ts)> wt_tuple(const tuple<Ts...> &t)
    {
        if (I)
            cout << ' ';
        wt(get<I>(t));
        wt_tuple<I + 1>(t);
    }
    template <class... Ts>
    void wt(const tuple<Ts...> &t) { wt_tuple(t); }

    // forward declarations (two-phase lookup for container elements)
    template <class T>
    void wt(const set<T> &s);
    template <class T>
    void wt(const multiset<T> &s);
    template <class T>
    void wt(const unordered_set<T> &s);
    template <class K, class V>
    void wt(const map<K, V> &m);
    template <class K, class V>
    void wt(const unordered_map<K, V> &m);
    template <class T, class Container, class Compare>
    void wt(const priority_queue<T, Container, Compare> &q);

    // array / vector / deque
    template <class T, size_t N>
    void wt(const array<T, N> &a)
    {
        for (size_t i = 0; i < N; i++)
        {
            if (i)
                cout << ' ';
            wt(a[i]);
        }
    }
    template <class T>
    void wt(const vector<T> &v)
    {
        for (size_t i = 0; i < v.size(); i++)
        {
            if (i)
                cout << ' ';
            wt(v[i]);
        }
    }
    template <class T>
    void wt(const vector<vector<T>> &v)
    {
        for (size_t i = 0; i < v.size(); i++)
        {
            if (i)
                cout << '\n';
            wt(v[i]);
        }
    }
    template <class T>
    void wt(const deque<T> &v)
    {
        for (size_t i = 0; i < v.size(); i++)
        {
            if (i)
                cout << ' ';
            wt(v[i]);
        }
    }
    template <class T, class Container, class Compare>
    void wt(const priority_queue<T, Container, Compare> &q)
    {
        auto qq = q;
        bool first = true;
        while (!qq.empty())
        {
            if (!first)
                cout << ' ';
            first = false;
            wt(qq.top());
            qq.pop();
        }
    }

    // set / multiset / unordered_set
    template <class T>
    void wt(const set<T> &s)
    {
        bool first = true;
        for (auto &x : s)
        {
            if (!first)
                cout << ' ';
            first = false;
            wt(x);
        }
    }
    template <class T>
    void wt(const multiset<T> &s)
    {
        bool first = true;
        for (auto &x : s)
        {
            if (!first)
                cout << ' ';
            first = false;
            wt(x);
        }
    }
    template <class T>
    void wt(const unordered_set<T> &s)
    {
        bool first = true;
        for (auto &x : s)
        {
            if (!first)
                cout << ' ';
            first = false;
            wt(x);
        }
    }

    // map / unordered_map
    template <class K, class V>
    void wt(const map<K, V> &m)
    {
        bool first = true;
        for (auto &kv : m)
        {
            if (!first)
                cout << " | ";
            first = false;
            wt(kv.first);
            cout << ':';
            wt(kv.second);
        }
    }
    template <class K, class V>
    void wt(const unordered_map<K, V> &m)
    {
        bool first = true;
        for (auto &kv : m)
        {
            if (!first)
                cout << " | ";
            first = false;
            wt(kv.first);
            cout << ':';
            wt(kv.second);
        }
    }

    // 出力本体
    void print() { cout << '\n'; }

    template <class Head, class... Tail>
    void print(const Head &head, const Tail &...tail)
    {
        wt(head);
        if (sizeof...(Tail))
            cout << ' ';
        print(tail...);
    }
} // namespace fastio

using fastio::print;
using fastio::read;

#define INT(...)     \
    int __VA_ARGS__; \
    read(__VA_ARGS__)
#define LL(...)     \
    ll __VA_ARGS__; \
    read(__VA_ARGS__)
#define U32(...)     \
    u32 __VA_ARGS__; \
    read(__VA_ARGS__)
#define U64(...)     \
    u64 __VA_ARGS__; \
    read(__VA_ARGS__)
#define STR(...)        \
    string __VA_ARGS__; \
    read(__VA_ARGS__)
#define CHAR(...)     \
    char __VA_ARGS__; \
    read(__VA_ARGS__)
#define DBL(...)        \
    double __VA_ARGS__; \
    read(__VA_ARGS__)
#define VEC(type, name, size) \
    vector<type> name(size);  \
    read(name)
#define VV(type, name, h, w)                       \
    vector<vector<type>> name(h, vector<type>(w)); \
    read(name)
#define VEC0(type, name, size) \
    vector<type> name(size)
#define VV0(type, name, h, w) \
    vector<vector<type>> name(h, vector<type>(w))
#define VECI(type, name, size, init) \
    vector<type> name(size, init)
#define VVI(type, name, h, w, init) \
    vector<vector<type>> name(h, vector<type>(w, init))

// ordered containers (set/multiset etc.) helpers:
// GE_IT(c, x): iterator to minimum element >= x
// LE_IT(c, x): iterator to maximum element <= x (or end if none)
template <class C, class T>
auto ge_it(const C &c, const T &x)
{
    return c.lower_bound(x);
}

template <class C, class T>
auto le_it(const C &c, const T &x)
{
    auto it = c.upper_bound(x);
    if (it == c.begin())
        return c.end();
    --it;
    return it;
}

template <class C, class T>
typename C::value_type ge_val(const C &c, const T &x)
{
    auto it = ge_it(c, x);
    if (it == c.end())
        throw out_of_range("GE_VAL: no element >= x");
    return *it;
}

template <class C, class T>
typename C::value_type le_val(const C &c, const T &x)
{
    auto it = le_it(c, x);
    if (it == c.end())
        throw out_of_range("LE_VAL: no element <= x");
    return *it;
}

template <class T, class Compare, class Alloc>
bool discard_one(set<T, Compare, Alloc> &s, const T &x)
{
    return s.erase(x) > 0;
}

template <class T, class Compare, class Alloc>
bool discard_one(multiset<T, Compare, Alloc> &s, const T &x)
{
    auto it = s.find(x);
    if (it == s.end())
        return false;
    s.erase(it); // erase only one
    return true;
}

template <class T, class Compare, class Alloc>
int discard_all(set<T, Compare, Alloc> &s, const T &x)
{
    return (int)s.erase(x); // 0 or 1
}

template <class T, class Compare, class Alloc>
int discard_all(multiset<T, Compare, Alloc> &s, const T &x)
{
    return (int)s.erase(x); // remove all x
}

#define GE_IT(c, x) ge_it((c), (x))
#define LE_IT(c, x) le_it((c), (x))
#define GE_VAL(c, x) ge_val((c), (x))
#define LE_VAL(c, x) le_val((c), (x))
#define DISCARD_ONE(c, x) discard_one((c), (x))
#define DISCARD_ALL(c, x) discard_all((c), (x))

// Python-like set operations for std::set:
// A | B, A & B, A - B, A ^ B and in-place variants.
template <class T, class CompareA, class AllocA, class CompareB, class AllocB>
set<T, CompareA, AllocA> operator|(const set<T, CompareA, AllocA> &a, const set<T, CompareB, AllocB> &b)
{
    set<T, CompareA, AllocA> res(a.begin(), a.end(), a.key_comp(), a.get_allocator());
    res.insert(b.begin(), b.end());
    return res;
}

template <class T, class CompareA, class AllocA, class CompareB, class AllocB>
set<T, CompareA, AllocA> operator&(const set<T, CompareA, AllocA> &a, const set<T, CompareB, AllocB> &b)
{
    set<T, CompareA, AllocA> res(a.key_comp(), a.get_allocator());
    for (const auto &x : a)
    {
        if (b.contains(x))
            res.insert(x);
    }
    return res;
}

template <class T, class CompareA, class AllocA, class CompareB, class AllocB>
set<T, CompareA, AllocA> operator-(const set<T, CompareA, AllocA> &a, const set<T, CompareB, AllocB> &b)
{
    set<T, CompareA, AllocA> res(a.key_comp(), a.get_allocator());
    for (const auto &x : a)
    {
        if (!b.contains(x))
            res.insert(x);
    }
    return res;
}

template <class T, class CompareA, class AllocA, class CompareB, class AllocB>
set<T, CompareA, AllocA> operator^(const set<T, CompareA, AllocA> &a, const set<T, CompareB, AllocB> &b)
{
    set<T, CompareA, AllocA> res = a - b;
    for (const auto &x : b)
    {
        if (!a.contains(x))
            res.insert(x);
    }
    return res;
}

template <class T, class CompareA, class AllocA, class CompareB, class AllocB>
set<T, CompareA, AllocA> &operator|=(set<T, CompareA, AllocA> &a, const set<T, CompareB, AllocB> &b)
{
    a = a | b;
    return a;
}

template <class T, class CompareA, class AllocA, class CompareB, class AllocB>
set<T, CompareA, AllocA> &operator&=(set<T, CompareA, AllocA> &a, const set<T, CompareB, AllocB> &b)
{
    a = a & b;
    return a;
}

template <class T, class CompareA, class AllocA, class CompareB, class AllocB>
set<T, CompareA, AllocA> &operator-=(set<T, CompareA, AllocA> &a, const set<T, CompareB, AllocB> &b)
{
    a = a - b;
    return a;
}

template <class T, class CompareA, class AllocA, class CompareB, class AllocB>
set<T, CompareA, AllocA> &operator^=(set<T, CompareA, AllocA> &a, const set<T, CompareB, AllocB> &b)
{
    a = a ^ b;
    return a;
}

template <class T, class CompareA, class AllocA, class CompareB, class AllocB>
bool is_subset(const set<T, CompareA, AllocA> &a, const set<T, CompareB, AllocB> &b)
{
    for (const auto &x : a)
    {
        if (!b.contains(x))
            return false;
    }
    return true;
}

template <class T, class CompareA, class AllocA, class CompareB, class AllocB>
bool is_superset(const set<T, CompareA, AllocA> &a, const set<T, CompareB, AllocB> &b)
{
    return is_subset(b, a);
}

template <class T, class CompareA, class AllocA, class CompareB, class AllocB>
bool is_disjoint(const set<T, CompareA, AllocA> &a, const set<T, CompareB, AllocB> &b)
{
    for (const auto &x : a)
    {
        if (b.contains(x))
            return false;
    }
    return true;
}

template <class T>
int bisect_left(const vector<T> &v, const T &x)
{
    return int(lower_bound(v.begin(), v.end(), x) - v.begin());
}

template <class T>
int bisect_right(const vector<T> &v, const T &x)
{
    return int(upper_bound(v.begin(), v.end(), x) - v.begin());
}

long long ipow(long long a, long long e)
{
    long long r = 1;
    while (e > 0)
    {
        if (e & 1)
            r *= a;
        a *= a;
        e >>= 1;
    }
    return r;
}

template <class It>
string join(It first, It last, const string &sep)
{
    ostringstream oss;
    bool first_elem = true;
    for (auto it = first; it != last; ++it)
    {
        if (!first_elem)
            oss << sep;
        first_elem = false;
        oss << *it;
    }
    return oss.str();
}

inline string join(const vector<string> &v, const string &sep)
{
    size_t total = 0;
    if (!v.empty())
        total = (v.size() - 1) * sep.size();
    for (const auto &s : v)
        total += s.size();
    string res;
    res.reserve(total);
    for (size_t i = 0; i < v.size(); ++i)
    {
        if (i)
            res += sep;
        res += v[i];
    }
    return res;
}

inline string join(const string &s, const string &sep)
{
    if (s.empty())
        return "";
    string res;
    if (!sep.empty())
        res.reserve(s.size() + (s.size() - 1) * sep.size());
    for (size_t i = 0; i < s.size(); ++i)
    {
        if (i)
            res += sep;
        res += s[i];
    }
    return res;
}

template <class C>
string join(const C &c, const string &sep)
{
    return join(c.begin(), c.end(), sep);
}

template <class C>
C reversed(C c)
{
    reverse(c.begin(), c.end());
    return c;
}

template <class T>
long long sum(const vector<T> &v)
{
    return accumulate(v.begin(), v.end(), 0LL);
}

struct Graph
{
    int n;
    vector<vector<int>> g;

    Graph(int n = 0) : n(n), g(n) {}

    void add_edge(int u, int v, bool undirected = true)
    {
        g[u].push_back(v);
        if (undirected)
            g[v].push_back(u);
    }

    vector<int> &operator[](int i) { return g[i]; }
    const vector<int> &operator[](int i) const { return g[i]; }
};

namespace combinatorial_enumeration_lib
{
    inline std::size_t count_combinations(int n, int r)
    {
        if (r < 0 || r > n)
            return 0;
        r = std::min(r, n - r);
        __int128 ways = 1;
        const __int128 max_size = static_cast<__int128>(std::numeric_limits<std::size_t>::max());
        for (int i = 1; i <= r; ++i)
        {
            ways = ways * (n - r + i) / i;
            if (ways > max_size)
                return std::numeric_limits<std::size_t>::max();
        }
        return static_cast<std::size_t>(ways);
    }

    inline std::size_t count_permutations(int n, int r)
    {
        if (r < 0 || r > n)
            return 0;
        __int128 ways = 1;
        const __int128 max_size = static_cast<__int128>(std::numeric_limits<std::size_t>::max());
        for (int i = 0; i < r; ++i)
        {
            ways *= (n - i);
            if (ways > max_size)
                return std::numeric_limits<std::size_t>::max();
        }
        return static_cast<std::size_t>(ways);
    }

    template <class T>
    void dfs_combinations(const std::vector<T> &items, int idx, int r,
                          std::vector<T> &current, std::vector<std::vector<T>> &result)
    {
        if (r == 0)
        {
            result.push_back(current);
            return;
        }
        if (idx == static_cast<int>(items.size()))
            return;
        if (static_cast<int>(items.size()) - idx < r)
            return;

        current.push_back(items[idx]);
        dfs_combinations(items, idx + 1, r - 1, current, result);
        current.pop_back();

        dfs_combinations(items, idx + 1, r, current, result);
    }

    template <class T>
    std::vector<std::vector<T>> combinations(const std::vector<T> &items, int r)
    {
        std::vector<std::vector<T>> result;
        if (r < 0 || r > static_cast<int>(items.size()))
            return result;

        result.reserve(count_combinations(static_cast<int>(items.size()), r));
        std::vector<T> current;
        current.reserve(r);
        dfs_combinations(items, 0, r, current, result);
        return result;
    }

    template <class T, class Callback>
    void dfs_combinations_callback(const std::vector<T> &items, int idx, int r,
                                   std::vector<T> &current, Callback &callback)
    {
        if (r == 0)
        {
            callback(current);
            return;
        }
        if (idx == static_cast<int>(items.size()))
            return;
        if (static_cast<int>(items.size()) - idx < r)
            return;

        current.push_back(items[idx]);
        dfs_combinations_callback(items, idx + 1, r - 1, current, callback);
        current.pop_back();

        dfs_combinations_callback(items, idx + 1, r, current, callback);
    }

    template <class T, class Callback>
    void for_each_combination(const std::vector<T> &items, int r, Callback &&callback)
    {
        if (r < 0 || r > static_cast<int>(items.size()))
            return;
        auto cb = std::forward<Callback>(callback);
        std::vector<T> current;
        current.reserve(r);
        dfs_combinations_callback(items, 0, r, current, cb);
    }

    template <class T>
    void dfs_permutations(const std::vector<T> &items, int r, std::vector<char> &used,
                          std::vector<T> &current, std::vector<std::vector<T>> &result)
    {
        if (static_cast<int>(current.size()) == r)
        {
            result.push_back(current);
            return;
        }

        for (int i = 0; i < static_cast<int>(items.size()); ++i)
        {
            if (used[i])
                continue;
            used[i] = 1;
            current.push_back(items[i]);
            dfs_permutations(items, r, used, current, result);
            current.pop_back();
            used[i] = 0;
        }
    }

    template <class T>
    std::vector<std::vector<T>> permutations(const std::vector<T> &items, int r)
    {
        std::vector<std::vector<T>> result;
        if (r < 0 || r > static_cast<int>(items.size()))
            return result;

        result.reserve(count_permutations(static_cast<int>(items.size()), r));
        std::vector<char> used(items.size(), 0);
        std::vector<T> current;
        current.reserve(r);
        dfs_permutations(items, r, used, current, result);
        return result;
    }

    template <class T>
    std::vector<std::vector<T>> permutations(const std::vector<T> &items)
    {
        return permutations(items, static_cast<int>(items.size()));
    }

    template <class T, class Callback>
    void dfs_permutations_callback(const std::vector<T> &items, int r, std::vector<char> &used,
                                   std::vector<T> &current, Callback &callback)
    {
        if (static_cast<int>(current.size()) == r)
        {
            callback(current);
            return;
        }

        for (int i = 0; i < static_cast<int>(items.size()); ++i)
        {
            if (used[i])
                continue;
            used[i] = 1;
            current.push_back(items[i]);
            dfs_permutations_callback(items, r, used, current, callback);
            current.pop_back();
            used[i] = 0;
        }
    }

    template <class T, class Callback>
    void for_each_permutation(const std::vector<T> &items, int r, Callback &&callback)
    {
        if (r < 0 || r > static_cast<int>(items.size()))
            return;

        auto cb = std::forward<Callback>(callback);
        std::vector<char> used(items.size(), 0);
        std::vector<T> current;
        current.reserve(r);
        dfs_permutations_callback(items, r, used, current, cb);
    }

    template <class T, class Callback>
    void for_each_permutation(const std::vector<T> &items, Callback &&callback)
    {
        for_each_permutation(items, static_cast<int>(items.size()), std::forward<Callback>(callback));
    }

    inline std::vector<int> range_values(int n)
    {
        std::vector<int> values;
        if (n < 0)
            return values;
        values.resize(n);
        for (int i = 0; i < n; ++i)
            values[i] = i;
        return values;
    }

    inline std::vector<std::vector<int>> combinations(int n, int r)
    {
        return combinations(range_values(n), r);
    }

    template <class Callback>
    void for_each_combination(int n, int r, Callback &&callback)
    {
        for_each_combination(range_values(n), r, std::forward<Callback>(callback));
    }

    inline std::vector<std::vector<int>> permutations(int n, int r)
    {
        return permutations(range_values(n), r);
    }

    inline std::vector<std::vector<int>> permutations(int n)
    {
        return permutations(range_values(n), n);
    }

    template <class Callback>
    void for_each_permutation(int n, int r, Callback &&callback)
    {
        for_each_permutation(range_values(n), r, std::forward<Callback>(callback));
    }

    template <class Callback>
    void for_each_permutation(int n, Callback &&callback)
    {
        for_each_permutation(range_values(n), n, std::forward<Callback>(callback));
    }
} // namespace combinatorial_enumeration_lib

int main()
{
    // 組み合わせの全列挙
    LL(h, w);
    VV(ll, A, h, w);
    LL(h2, w2);
    VV(ll, B, h2, w2);
    // print(A);
    // print(B);
    vector<ll> W, H;
    rep0(i, w)
    {
        W.push_back(i);
    }
    rep0(i, h)
    {
        H.push_back(i);
    }
    vector<vector<ll>> Wc = combinatorial_enumeration_lib::combinations(W, w2);
    vector<vector<ll>> Hc = combinatorial_enumeration_lib::combinations(H, h2);
    for (vector<ll> wc : Wc)
    {
        for (vector<ll> hc : Hc)
        {
            VV0(ll, C, h2, w2);
            // print(hc);
            // print(wc);
            rep0(i, h2)
            {
                rep0(j, w2)
                {
                    C[i][j] = A[hc[i]][wc[j]];
                }
            }
            if (C == B)
            {
                print("Yes");
                return 0;
            }
            // print(C);
            // print("-------------------");
        }
    }
    print("No");
}
